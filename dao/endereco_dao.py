from dao import Endereco


class EnderecoDAO:
    def __init__(self, db_conn):
        self._db_conn = db_conn

    def pegar_endereco_por_id_usuario(self, usuario_id: int) -> Endereco:
        endereco: Endereco = self._db_conn.query(Endereco).filter(Endereco.fk_id_usuario == usuario_id).first()
        return endereco

    def registrar_endereco(self, endereco:  Endereco):
        try:
            self._db_conn.add(endereco)
            self._db_conn.commit()
        except RuntimeError:
            self._db_conn.rollback()
        finally:
            self._db_conn.close()

    def alterar_endereco(self, endereco_id: int, novas_info_endereco: Endereco):
        try:
            self._db_conn.query(Endereco).filter(Endereco.endereco_id == endereco_id).update({
                Endereco.pais_do_usuario: novas_info_endereco.pais_do_usuario,
                Endereco.estado_do_usuario: novas_info_endereco.estado_do_usuario,
                Endereco.municipio_do_usuario: novas_info_endereco.municipio_do_usuario,
                Endereco.cep_do_usuario: novas_info_endereco.cep_do_usuario,
                Endereco.rua_do_usuario: novas_info_endereco.rua_do_usuario,
                Endereco.numero_da_rua: novas_info_endereco.numero_da_rua,
                Endereco.complemento: novas_info_endereco.complemento
            })
            self._db_conn.commit()
        except RuntimeError:
            self._db_conn.rollback()
        finally:
            self._db_conn.close()

    def deletar_endereco(self, endereco_id: int):
        self._db_conn.query(Endereco).filter(Endereco.endereco_id == endereco_id).delete()
        self._db_conn.commit()
