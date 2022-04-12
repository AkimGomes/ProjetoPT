from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario
from db import db_session


usuario_dao = UsuarioDAO(db_session)


def test_registrar_usuario_e_buscar_por_id_no_banco():
    usuario = Usuario('teste',
                      'teste@gmail.com',
                      'teste',
                      '000.000.000-00',
                      '000.00000.00-0')
    usuario_dao.registrar_usuario(usuario)
    usuario_id = usuario.id
    resultado_da_pesquisa_no_banco = usuario_dao.pegar_usuario_id(usuario_id)
    assert resultado_da_pesquisa_no_banco is not None


def test_alterar_usuario_cadastrado_no_banco_recebendo_novas_info():
    usuario = Usuario('teste',
                      'teste@gmail.com',
                      'teste',
                      '000.000.000-00',
                      '000.00000.00-0')
    usuario_dao.registrar_usuario(usuario)
    usuario_id = usuario.id
    usuario_1 = Usuario('teste1',
                        'teste1@gmail.com',
                        'teste1',
                        '111.111.111-11',
                        '111.11111.11-1')
    usuario_dao.alterar_usuario(usuario_id, usuario_1)
    resultado_da_pesquisa_no_banco = usuario_dao.pegar_usuario_id(usuario_id)
    assert resultado_da_pesquisa_no_banco is not None


def test_deletar_usuario_cadastrado_por_id_do_usuario():
    usuario = Usuario('teste',
                      'teste@gmail.com',
                      'teste',
                      '000.000.000-00',
                      '000.00000.00-0')
    usuario_dao.registrar_usuario(usuario)
    usuario_id = usuario.id
    usuario_dao.deletar_usuario(usuario_id)
    resultado_da_pesquisa_no_banco = usuario_dao.pegar_usuario_id(usuario_id)
    assert resultado_da_pesquisa_no_banco is None


def test_buscar_por_email_no_banco_por_email_inserido_no_login():
    login = 'teste@gmail.com'
    resultado_da_pesquisa_no_banco = usuario_dao.pegar_usuario_login_email(login)
    assert resultado_da_pesquisa_no_banco is not None


def test_buscar_por_cpf_no_banco_por_cpf_inserido_no_login():
    cpf = '111.111.111-11'
    resultado_da_pesquisa_no_banco = usuario_dao.pegar_usuario_login_cpf(cpf)
    assert resultado_da_pesquisa_no_banco is not None


def test_buscar_por_pis_no_banco_por_pis_inserido_no_login():
    pis = '111.11111.11-1'
    resultado_da_pesquisa_no_banco = usuario_dao.pegar_usuario_login_pis(pis)
    assert resultado_da_pesquisa_no_banco is not None




