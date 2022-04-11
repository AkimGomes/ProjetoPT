from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequestKeyError

from modules.db import Usuario, Endereco, db_session

from modules.dao.usuario_dao import UsuarioDAO
from modules.dao.endereco_dao import EnderecoDAO

app = Flask(__name__)
app.secret_key = "ProjetoPT"

login_manager = LoginManager(app)
login_manager.login_view = ''
login_manager.login_message = "Por favor, faça o login para acessar o sistema!"

usuario_dao = UsuarioDAO(db_session)
endereco_dao = EnderecoDAO(db_session)


@login_manager.user_loader
def load_user(usuario_id):
    return usuario_dao.pega_usuario_id(usuario_id)


@app.route('/inicio', methods=['GET', 'POST'])
def loga_usuario():
    if request.method == 'POST':
        usuario = usuario_dao.pega_usuario_login_email(request.form['login'])
        usuario_cpf = usuario_dao.pega_usuario_login_cpf(request.form['login'])
        usuario_pis = usuario_dao.pega_usuario_login_pis(request.form['login'])
        senha = request.form['password']
        return _loga_usuario_no_sistema(usuario, usuario_cpf, usuario_pis, senha)
    return render_template('loga_usuario.html')


def _loga_usuario_no_sistema(usuario, usuario_cpf, usuario_pis, senha):
    if _verifica_email_e_senha_do_usuario(usuario, senha):
        login_user(usuario)
        return redirect(url_for('mostra_menu_usuario', usuario_id=usuario.id))
    if _verifica_cpf_e_senha_do_usuario(usuario_cpf, senha):
        login_user(usuario_cpf)
        return redirect(url_for('mostra_menu_usuario', usuario_id=usuario_cpf.id))
    if _verifica_pis_e_senha_do_usuario(usuario_pis, senha):
        login_user(usuario_pis)
        return redirect(url_for('mostra_menu_usuario', usuario_id=usuario_pis.id))
    else:
        flash('Usuário ou senha inválidos!(CPF=000.000.000-00, PIS=000.00000.00-0)', 'error')
        return redirect(url_for('loga_usuario'))


def _verifica_email_e_senha_do_usuario(usuario, senha):
    return usuario and check_password_hash(usuario.senha_do_usuario, senha)


def _verifica_cpf_e_senha_do_usuario(usuario, senha):
    return usuario and check_password_hash(usuario.senha_do_usuario, senha)


def _verifica_pis_e_senha_do_usuario(usuario, senha):
    return usuario and check_password_hash(usuario.senha_do_usuario, senha)


@app.route('/registra-usuario', methods=['GET', 'POST'])
def registra_usuario():
    if request.method == 'POST':
        try:
            return _registra_usuario_no_sistema()
        except IntegrityError:
            flash('Erro. CPF, PIS ou E-mail já cadastrados por outro usuário!', 'error')
        except BadRequestKeyError:
            flash('Por favor, preencha os dados de Pais e Estado', 'error')
    return render_template('registra_usuario.html')


def _registra_usuario_no_sistema():
    usuario = Usuario(request.form['nome'],
                      request.form['email'],
                      generate_password_hash(request.form['senha']),
                      request.form['cpf'],
                      request.form['pis'])
    usuario_dao.registra_usuario(usuario)
    endereco = Endereco(usuario.id,
                        request.form['pais'],
                        request.form['estado'],
                        request.form['municipio'],
                        request.form['cep'],
                        request.form['rua'],
                        request.form['numero'],
                        request.form['complemento'])
    endereco_dao.registra_endereco(endereco)
    flash('Usuário cadastrado com sucesso!', 'success')
    return redirect(url_for('loga_usuario'))


@app.route('/edita-info-do-usuario', methods=['GET', 'POST'])
@login_required
def edita_info_do_usuario():
    if request.method == 'POST':
        try:
            return _aplica_edicoes_de_info_do_usuario()
        except IntegrityError:
            flash('Erro. CPF, PIS ou E-mail já cadastrados por outro usuário!', 'error')
        except BadRequestKeyError:
            flash('Por favor, preencha os dados de Pais e Estado', 'error')
    endereco = endereco_dao.pega_endereco_por_id_usuario(request.args.get('usuario_id'))
    return render_template('edita_info_do_usuario.html', endereco=endereco)


def _aplica_edicoes_de_info_do_usuario():
    usuario = Usuario(request.form['nome'],
                      request.form['email'],
                      generate_password_hash(request.form['senha']),
                      request.form['cpf'],
                      request.form['pis'])
    usuario_dao.altera_usuario(request.args.get('usuario_id'), usuario)
    endereco = Endereco(usuario.id,
                        request.form['pais'],
                        request.form['estado'],
                        request.form['municipio'],
                        request.form['cep'],
                        request.form['rua'],
                        request.form['numero'],
                        request.form['complemento'])
    endereco_dao.altera_endereco(request.args.get('endereco_id'), endereco)
    flash('Alterações feitas com sucesso!', 'success')
    return redirect(url_for('mostra_menu_usuario', usuario_id=request.args.get('usuario_id')))


@app.route('/desloga-usuario')
@login_required
def desloga_usuario():
    logout_user()
    flash('Usuário deslogado com sucesso!', 'success')
    return redirect(url_for('loga_usuario'))


@app.route('/deleta-usuario')
@login_required
def deleta_usuario():
    endereco_dao.deleta_endereco(request.args.get('usuario_id'))
    usuario_dao.deleta_usuario(request.args.get('usuario_id'))
    flash('Usuário removido com sucesso!', 'success')
    return redirect(url_for('loga_usuario'))


@app.route('/menu-usuario', methods=['GET', 'POST'])
@login_required
def mostra_menu_usuario():
    endereco = endereco_dao.pega_endereco_por_id_usuario(request.args.get('usuario_id'))
    return render_template('mostra_menu_usuario.html', endereco=endereco)


app.run(debug=True)
