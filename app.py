from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, logout_user, login_required
from sqlalchemy.exc import IntegrityError

from werkzeug.exceptions import BadRequestKeyError

from controllers import usuario_dao
from controllers.endereco_controller import pegar_endereco_por_id_do_usuario

app = Flask(__name__)
app.secret_key = "ProjetoPT"

login_manager = LoginManager(app)
login_manager.login_view = ''
login_manager.login_message = "Por favor, faça o login para acessar o sistema!"


@login_manager.user_loader
def load_user(usuario_id):
    return usuario_dao.pega_usuario_id(usuario_id)


@app.route('/inicio', methods=['GET', 'POST'])
def loga_usuario():
    from controllers.usuario_controller import loga_usuario_no_sistema, pegar_login_e_senha_do_usuario

    if request.method == 'POST':
        usuario, usuario_cpf, usuario_pis, senha = pegar_login_e_senha_do_usuario(request)
        return loga_usuario_no_sistema(usuario, usuario_cpf, usuario_pis, senha)
    return render_template('loga_usuario.html')


@app.route('/registra-usuario', methods=['GET', 'POST'])
def registra_usuario():
    if request.method == 'POST':
        from controllers.usuario_controller import registra_usuario_no_sistema
        from controllers.endereco_controller import registra_endereco_no_sistema

        try:
            usuario_id = registra_usuario_no_sistema(request)
            registra_endereco_no_sistema(request, usuario_id)
            flash('Usuário cadastrado com sucesso!', 'success')
            return redirect(url_for('loga_usuario'))
        except IntegrityError:
            flash('Erro. CPF, PIS ou E-mail já cadastrados por outro usuário!', 'error')
        except BadRequestKeyError:
            flash('Por favor, preencha os dados de Pais e Estado', 'error')
    return render_template('registra_usuario.html')


@app.route('/edita-info-do-usuario', methods=['GET', 'POST'])
@login_required
def edita_info_do_usuario():
    if request.method == 'POST':
        try:
            from controllers.usuario_controller import aplica_edicoes_de_info_do_usuario
            from controllers.endereco_controller import aplica_edicoes_de_info_do_endereco

            usuario_id = aplica_edicoes_de_info_do_usuario(request)
            aplica_edicoes_de_info_do_endereco(request, usuario_id)
            flash('Alterações feitas com sucesso!', 'success')
            return redirect(url_for('mostra_menu_usuario', usuario_id=request.args.get('usuario_id')))
        except IntegrityError:
            flash('Erro. CPF, PIS ou E-mail já cadastrados por outro usuário!', 'error')
        except BadRequestKeyError:
            flash('Por favor, preencha os dados de Pais e Estado', 'error')
    endereco = pegar_endereco_por_id_do_usuario(request)
    return render_template('edita_info_do_usuario.html', endereco=endereco)


@app.route('/desloga-usuario')
@login_required
def desloga_usuario():
    logout_user()
    flash('Usuário deslogado com sucesso!', 'success')
    return redirect(url_for('loga_usuario'))


@app.route('/deleta-usuario')
@login_required
def deleta_usuario():
    from controllers.endereco_controller import deleta_endereco_por_id
    from controllers.usuario_controller import deleta_usuario_por_id

    deleta_endereco_por_id(request)
    deleta_usuario_por_id(request)
    flash('Usuário removido com sucesso!', 'success')
    return redirect(url_for('loga_usuario'))


@app.route('/menu-usuario', methods=['GET', 'POST'])
@login_required
def mostra_menu_usuario():
    endereco = pegar_endereco_por_id_do_usuario(request)
    return render_template('mostra_menu_usuario.html', endereco=endereco)


app.run(debug=True)
