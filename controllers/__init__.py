from db import db_session
from dao.usuario_dao import UsuarioDAO
from dao.endereco_dao import EnderecoDAO

usuario_dao = UsuarioDAO(db_session)
endereco_dao = EnderecoDAO(db_session)
