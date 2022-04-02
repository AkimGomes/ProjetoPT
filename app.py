from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.exc import IntegrityError, DataError

from modules.db import Usuario, Endereco, db_session
from modules.dao.usuario_dao import UsuarioDAO
from modules.dao.endereco_dao import EnderecoDAO

app = Flask(__name__)
app.secret_key = "ProjetoTPT"

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
        usuario_cpf = usuario_dao.pega_usuario_cpf(request.form['login'])
        usuario_pis = usuario_dao.pega_usuario_pis(request.form['login'])
        senha = request.form['password']
        if usuario and check_password_hash(usuario.senha_do_usuario, senha):
            login_user(usuario)
            return redirect(url_for('mostra_menu_usuario'))
        if usuario_cpf and check_password_hash(usuario_cpf.senha_do_usuario, senha):
            login_user(usuario_cpf)
            return redirect(url_for('mostra_menu_usuario'))
        if usuario_pis and check_password_hash(usuario_pis.senha_do_usuario, senha):
            login_user(usuario_pis)
            return redirect(url_for('mostra_menu_usuario'))
        else:
            flash('Usuário ou senha inválidos!', 'error')
            return redirect(url_for('loga_usuario'))
    return render_template('inicio.html')


@app.route('/registra-usuario', methods=['GET', 'POST'])
def registra_usuario():
    if request.method == 'POST':
        pis = usuario_dao.pega_usuario_pis(request.form['pis'])
        cpf = usuario_dao.pega_usuario_cpf(request.form['cpf'])
        email = usuario_dao.pega_usuario_email(request.form['email'])
        if pis or cpf or email:
            flash('Dados inválidos. CPF, PIS ou Email já cadastrados!', 'error')
        else:
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
    return render_template('cadastro_de_usuario.html')


@app.route('/informacoes-editaveis-do-usuario', methods=['GET', 'POST'])
@login_required
def edita_info_do_usuario():
    if request.method == 'POST':
        usuario = Usuario(request.form['nome'],
                          request.form['email'],
                          request.form['cpf'],
                          request.form['pis'])
        usuario_dao.altera_usuario(usuario.id, usuario)
        endereco = Endereco(usuario.id,
                            request.form['pais'],
                            request.form['estado'],
                            request.form['municipio'],
                            request.form['cep'],
                            request.form['rua'],
                            request.form['numero'],
                            request.form['complemento'])
        endereco_dao.altera_endereco(endereco.endereco_id, endereco)
        flash('Alterações feitas com sucesso!')
        return redirect(url_for('mostra_menu_usuario'))
    return render_template('informacoes_do_usuario_logado.html')


@app.route('/desloga-usuario')
@login_required
def desloga_usuario():
    logout_user()
    flash('Usuário deslogado com sucesso!', 'success')
    return redirect(url_for('loga_usuario'))


@app.route('/deleta-usuario')
@login_required
def deleta_usuario():
    usuario_dao.deleta_usuario(request.args.get('id'))
    endereco_dao.deleta_endereco(request.args.get('id'))
    flash('Usuário removido com sucesso!', 'success')
    return redirect(url_for('loga_usuario'))


@app.route('/menu-usuario')
@login_required
def mostra_menu_usuario():
    return render_template('usuario_logado.html')


app.run(debug=True)
