from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, logout_user, login_required
from sqlalchemy.exc import IntegrityError

from werkzeug.exceptions import BadRequestKeyError

from controllers import usuario_dao
from controllers.endereco_controller import pegar_endereco_por_id_do_usuario
from models.endereco import Endereco

app = Flask(__name__)
app.secret_key = "ProjetoPT"

login_manager: LoginManager = LoginManager(app)
login_manager.login_view = ''
login_manager.login_message = "Por favor, faça o login para acessar o sistema!"


@login_manager.user_loader
def load_user(usuario_id):
    return usuario_dao.pegar_usuario_id(usuario_id)


@app.route('/inicio', methods=['GET', 'POST'])
def logar_usuario():
    from controllers.usuario_controller import logar_usuario_no_sistema, pegar_login_e_senha_do_usuario

    if request.method == 'POST':
        (
            usuario_email,
            usuario_cpf,
            usuario_pis,
            senha
        ) = pegar_login_e_senha_do_usuario(request)
        return logar_usuario_no_sistema(usuario_email, usuario_cpf, usuario_pis, senha)
    return render_template('logar_usuario.html')


@app.route('/registrar-usuario', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':
        from controllers.usuario_controller import registrar_usuario_no_sistema
        from controllers.endereco_controller import registrar_endereco_no_sistema

        try:
            usuario_id: int = registrar_usuario_no_sistema(request)
            registrar_endereco_no_sistema(request, usuario_id)
            flash('Usuário cadastrado com sucesso!', 'success')
            return redirect(url_for('logar_usuario'))
        except IntegrityError:
            flash('Erro. CPF, PIS ou E-mail já cadastrados por outro usuário!', 'error')
        except BadRequestKeyError:
            flash('Por favor, preencha os dados de Pais e Estado', 'error')
    return render_template('registrar_usuario.html')


@app.route('/editar-info-do-usuario', methods=['GET', 'POST'])
@login_required
def editar_info_do_usuario():
    if request.method == 'POST':
        try:
            from controllers.usuario_controller import aplicar_edicoes_de_info_do_usuario
            from controllers.endereco_controller import aplicar_edicoes_de_info_do_endereco

            usuario_id: int = aplicar_edicoes_de_info_do_usuario(request)
            aplicar_edicoes_de_info_do_endereco(request, usuario_id)
            flash('Alterações feitas com sucesso!', 'success')
            return redirect(url_for('mostrar_menu_usuario', usuario_id=request.args.get('usuario_id')))
        except IntegrityError:
            flash('Erro. CPF, PIS ou E-mail já cadastrados por outro usuário!', 'error')
        except BadRequestKeyError:
            flash('Por favor, preencha os dados de Pais e Estado', 'error')
    endereco_usuario: Endereco = pegar_endereco_por_id_do_usuario(request)
    return render_template('editar_info_do_usuario.html', endereco=endereco_usuario)


@app.route('/deslogar-usuario')
@login_required
def deslogar_usuario():
    logout_user()
    flash('Usuário deslogado com sucesso!', 'success')
    return redirect(url_for('logar_usuario'))


@app.route('/deletar-usuario')
@login_required
def deletar_usuario():
    from controllers.endereco_controller import deletar_endereco_por_id
    from controllers.usuario_controller import deletar_usuario_por_id

    deletar_endereco_por_id(request)
    deletar_usuario_por_id(request)
    flash('Usuário removido com sucesso!', 'success')
    return redirect(url_for('logar_usuario'))


@app.route('/mostrar-menu-usuario', methods=['GET', 'POST'])
@login_required
def mostrar_menu_usuario():
    endereco_usuario: Endereco = pegar_endereco_por_id_do_usuario(request)
    return render_template('mostrar_menu_usuario.html', endereco=endereco_usuario)


app.run(debug=True)
