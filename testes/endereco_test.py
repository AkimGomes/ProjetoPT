from dao.usuario_dao import UsuarioDAO
from dao.endereco_dao import EnderecoDAO
from models.usuario import Usuario
from models.endereco import Endereco
from db import db_session

usuario_dao = UsuarioDAO(db_session)
endereco_dao = EnderecoDAO(db_session)


def test_registrar_usuario_e_endereco_e_buscar_endereco_por_id_do_usuario():
    usuario = Usuario('teste',
                      'teste@gmail.com',
                      'teste',
                      '000.000.000-00',
                      '000.00000.00-0')
    usuario_dao.registrar_usuario(usuario)
    usuario_id = usuario.id
    endereco = Endereco(usuario_id,
                        'BR',
                        'São Paulo',
                        'São Paulo',
                        '02317-100',
                        'Rua Teste',
                        111,
                        'Apto 62')
    endereco_dao.registrar_endereco(endereco)
    resultado_da_pesquisa_no_banco = endereco_dao.pegar_endereco_por_id_usuario(usuario_id)
    assert resultado_da_pesquisa_no_banco is not None


def test_alterar_endereco_por_id_do_usuario():
    usuario1 = Usuario('teste',
                       'teste@gmail.com',
                       'teste',
                       '000.000.000-00',
                       '000.00000.00-0')
    usuario_dao.registrar_usuario(usuario1)
    usuario_id = usuario1.id
    endereco1 = Endereco(usuario_id,
                         'BR',
                         'São Paulo',
                         'São Paulo',
                         '02317-100',
                         'Rua Teste',
                         111,
                         'Apto 62')
    endereco_dao.registrar_endereco(endereco1)

    endereco2 = Endereco(usuario_id,
                         'BR',
                         'Acre',
                         'Rio Branco',
                         '02317-100',
                         'Rua Teste2',
                         222,
                         'apto 22')
    endereco_dao.alterar_endereco(usuario_id, endereco2)
    resultado_da_pesquisa_no_banco = endereco_dao.pegar_endereco_por_id_usuario(usuario_id)
    assert resultado_da_pesquisa_no_banco is not None


def test_deletar_endereco_por_id_do_usuario():
    usuario = Usuario('teste',
                      'teste@gmail.com',
                      'teste',
                      '000.000.000-00',
                      '000.00000.00-0')
    usuario_dao.registrar_usuario(usuario)
    usuario_id = usuario.id
    endereco = Endereco(usuario_id,
                        'BR',
                        'São Paulo',
                        'São Paulo',
                        '02317-100',
                        'Rua Teste',
                        111,
                        'Apto 62')
    endereco_dao.registrar_endereco(endereco)
    endereco_dao.deletar_endereco(usuario_id)
    resultado_da_pesquisa_no_banco = endereco_dao.pegar_endereco_por_id_usuario(usuario_id)
    assert resultado_da_pesquisa_no_banco is None
