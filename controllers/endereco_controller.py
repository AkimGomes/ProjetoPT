from models.endereco import Endereco
from controllers import endereco_dao


def registra_endereco_no_sistema(request, usuario_id):
    endereco = Endereco(usuario_id,
                        request.form['pais'],
                        request.form['estado'],
                        request.form['municipio'],
                        request.form['cep'],
                        request.form['rua'],
                        request.form['numero'],
                        request.form['complemento'])
    endereco_dao.registra_endereco(endereco)


def pegar_endereco_por_id_do_usuario(request):
    endereco = endereco_dao.pega_endereco_por_id_usuario(request.args.get('usuario_id'))
    return endereco


def aplica_edicoes_de_info_do_endereco(request, usuario_id):
    endereco = Endereco(usuario_id,
                        request.form['pais'],
                        request.form['estado'],
                        request.form['municipio'],
                        request.form['cep'],
                        request.form['rua'],
                        request.form['numero'],
                        request.form['complemento'])
    endereco_dao.altera_endereco(request.args.get('endereco_id'), endereco)


def deleta_endereco_por_id(request):
    endereco_dao.deleta_endereco(request.args.get('usuario_id'))
