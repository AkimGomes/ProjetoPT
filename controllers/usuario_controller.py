from flask import url_for, flash, Request
from flask_login import login_user
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash, generate_password_hash
from typing import Union
from werkzeug.wrappers.response import Response

from controllers import usuario_dao
from models.usuario import Usuario


def pegar_login_e_senha_do_usuario(requisicao: Request):
    usuario_email: Union[Usuario, None] = usuario_dao.pegar_usuario_login_email(requisicao.form['login'])
    usuario_cpf: Union[Usuario, None] = usuario_dao.pegar_usuario_login_cpf(requisicao.form['login'])
    usuario_pis: Union[Usuario, None] = usuario_dao.pegar_usuario_login_pis(requisicao.form['login'])
    senha: str = requisicao.form['password']
    return usuario_email, usuario_cpf, usuario_pis, senha


def logar_usuario_no_sistema(
        usuario_email: Union[Usuario, None],
        usuario_cpf: Union[Usuario, None],
        usuario_pis: Union[Usuario, None],
        senha: Union[str, None]
) -> Response:
    if _verificar_email_e_senha_do_usuario(usuario_email, senha):
        login_user(usuario_email)
        return redirect(url_for('mostrar_menu_usuario', usuario_id=usuario_email.id))
    if _verificar_cpf_e_senha_do_usuario(usuario_cpf, senha):
        login_user(usuario_cpf)
        return redirect(url_for('mostrar_menu_usuario', usuario_id=usuario_cpf.id))
    if _verificar_pis_e_senha_do_usuario(usuario_pis, senha):
        login_user(usuario_pis)
        return redirect(url_for('mostrar_menu_usuario', usuario_id=usuario_pis.id))
    else:
        flash('Usuário ou senha inválidos!(CPF=000.000.000-00, PIS=000.00000.00-0)', 'error')
        return redirect(url_for('logar_usuario'))


def _verificar_email_e_senha_do_usuario(usuario: Usuario, senha: str) -> tuple[Usuario, bool]:
    return usuario and check_password_hash(usuario.senha_do_usuario, senha)


def _verificar_cpf_e_senha_do_usuario(usuario: Usuario, senha: str) -> tuple[Usuario, bool]:
    return usuario and check_password_hash(usuario.senha_do_usuario, senha)


def _verificar_pis_e_senha_do_usuario(usuario: Usuario, senha: str) -> tuple[Usuario, bool]:
    return usuario and check_password_hash(usuario.senha_do_usuario, senha)


def registrar_usuario_no_sistema(requisicao: Request) -> int:
    usuario = Usuario(requisicao.form['nome'],
                      requisicao.form['email'],
                      generate_password_hash(requisicao.form['senha']),
                      requisicao.form['cpf'],
                      requisicao.form['pis'])
    usuario_dao.registrar_usuario(usuario)
    usuario_id: int = usuario.id
    return usuario_id


def aplicar_edicoes_de_info_do_usuario(requisicao: Request) -> int:
    usuario = Usuario(requisicao.form['nome'],
                      requisicao.form['email'],
                      generate_password_hash(requisicao.form['senha']),
                      requisicao.form['cpf'],
                      requisicao.form['pis'])
    usuario_dao.alterar_usuario(requisicao.args.get('usuario_id'), usuario)
    usuario_id: int = usuario.id
    return usuario_id


def deletar_usuario_por_id(requisicao: Request):
    usuario_dao.deletar_usuario(requisicao.args.get('usuario_id'))
