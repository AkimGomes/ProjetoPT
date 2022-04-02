from modules.db import Usuario


class UsuarioDAO:
    def __init__(self, db_conn):
        self._db_conn = db_conn

    def pega_usuario_id(self, usuario_id):
        usuario_id = self._db_conn.query(Usuario).filter(Usuario.id == usuario_id).first()
        return usuario_id

    def pega_usuario_login(self, usuario):
        usuario = self._db_conn.query(Usuario).filter(Usuario.email_do_usuario == usuario).first()
        return usuario

    def registra_usuario(self, usuario):
        try:
            self._db_conn.add(usuario)
            self._db_conn.commit()
        except RuntimeError:
            self._db_conn.rollback()
        finally:
            self._db_conn.close()

    def altera_usuario(self, usuario_id, novas_info_usuario):
        try:
            self._db_conn.query(Usuario).filter(Usuario.id == usuario_id).update({
                Usuario.nome_do_usuario: novas_info_usuario.nome_do_usuario,
                Usuario.email_do_usuario: novas_info_usuario.email_do_usuario,
                Usuario.senha_do_usuario: novas_info_usuario.senha_do_usuario,
                Usuario.cpf_do_usuario: novas_info_usuario.cpf_do_usuario,
                Usuario.pis_do_usuario: novas_info_usuario.pis_do_usuario
            })
            self._db_conn.commit()
        except RuntimeError:
            self._db_conn.rollback()
        finally:
            self._db_conn.close()

    def deleta_usuario(self, usuario_id):
        self._db_conn.query(Usuario).filter(Usuario.id == usuario_id).delete()
        self._db_conn.commit()
