from flask import Request

from models.endereco import Endereco
from controllers import endereco_dao


def registrar_endereco_no_sistema(requisicao: Request, usuario_id: int):
    endereco = Endereco(usuario_id,
                        requisicao.form['pais'],
                        requisicao.form['estado'],
                        requisicao.form['municipio'],
                        requisicao.form['cep'],
                        requisicao.form['rua'],
                        requisicao.form['numero'],
                        requisicao.form['complemento'])
    endereco_dao.registrar_endereco(endereco)


def pegar_endereco_por_id_do_usuario(requisicao: Request):
    endereco: Endereco = endereco_dao.pegar_endereco_por_id_usuario(requisicao.args.get('usuario_id'))
    return endereco


def aplicar_edicoes_de_info_do_endereco(requisicao: Request, usuario_id: int):
    endereco = Endereco(usuario_id,
                        requisicao.form['pais'],
                        requisicao.form['estado'],
                        requisicao.form['municipio'],
                        requisicao.form['cep'],
                        requisicao.form['rua'],
                        requisicao.form['numero'],
                        requisicao.form['complemento'])
    endereco_dao.alterar_endereco(requisicao.args.get('endereco_id'), endereco)


def deletar_endereco_por_id(requisicao: Request):
    endereco_dao.deletar_endereco(requisicao.args.get('usuario_id'))
