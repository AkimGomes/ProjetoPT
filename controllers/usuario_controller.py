from flask import url_for, flash
from flask_login import login_user
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash

from controllers import usuario_dao


def pegar_login_e_senha_do_usuario(request):
    usuario = usuario_dao.pega_usuario_login_email(request.form['login'])
    usuario_cpf = usuario_dao.pega_usuario_login_cpf(request.form['login'])
    usuario_pis = usuario_dao.pega_usuario_login_pis(request.form['login'])
    senha = request.form['password']
    return usuario, usuario_cpf, usuario_pis, senha


def loga_usuario_no_sistema(usuario, usuario_cpf, usuario_pis, senha):
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
