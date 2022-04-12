from testes import usuario_dao, Usuario, db_session
from dao.endereco_dao import EnderecoDAO
from models.endereco import Endereco


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
    endereco_dao.deletar_endereco(usuario_id)
    usuario_dao.deletar_usuario(usuario_id)


def test_alterar_endereco_por_id_do_usuario():
    usuario1 = Usuario('teste',
                       'teste1@gmail.com',
                       'teste',
                       '111.111.111-11',
                       '111.11111.11-1')
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
    endereco_dao.deletar_endereco(usuario_id)
    usuario_dao.deletar_usuario(usuario_id)


def test_deletar_endereco_por_id_do_usuario():
    usuario = Usuario('teste',
                      'teste2@gmail.com',
                      'teste',
                      '222.222.222-22',
                      '222.22222.22-2')
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
    usuario_dao.deletar_usuario(usuario_id)
    resultado_da_pesquisa_no_banco = endereco_dao.pegar_endereco_por_id_usuario(usuario_id)
    assert resultado_da_pesquisa_no_banco is None
