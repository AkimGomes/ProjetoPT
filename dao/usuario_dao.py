from dao import Usuario


class UsuarioDAO:
    def __init__(self, db_conn):
        self._db_conn = db_conn

    def pegar_usuario_id(self, usuario_id: int) -> int:
        usuario_id: int = self._db_conn.query(Usuario).filter(Usuario.id == usuario_id).first()
        return usuario_id

    def pegar_usuario_login_email(self, usuario: str) -> Usuario:
        usuario: Usuario = self._db_conn.query(Usuario).filter(Usuario.email_do_usuario == usuario).first()
        return usuario

    def pegar_usuario_login_cpf(self, usuario: str) -> Usuario:
        usuario: Usuario = self._db_conn.query(Usuario).filter(Usuario.cpf_do_usuario == usuario).first()
        return usuario

    def pegar_usuario_login_pis(self, usuario: str) -> Usuario:
        usuario: Usuario = self._db_conn.query(Usuario).filter(Usuario.pis_do_usuario == usuario).first()
        return usuario

    def registrar_usuario(self, usuario: Usuario):
        try:
            self._db_conn.add(usuario)
            self._db_conn.commit()
        except RuntimeError:
            self._db_conn.rollback()
        finally:
            self._db_conn.close()

    def alterar_usuario(self, usuario_id: int, novas_info_usuario: Usuario):
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

    def deletar_usuario(self, usuario_id: int):
        self._db_conn.query(Usuario).filter(Usuario.id == usuario_id).delete()
        self._db_conn.commit()
