from db import db_session
from dao.usuario_dao import UsuarioDAO

usuario_dao = UsuarioDAO(db_session)
