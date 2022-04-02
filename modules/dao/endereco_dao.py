from modules.db import Endereco


class EnderecoDAO:
    def __init__(self, db_conn):
        self._db_conn = db_conn

    def pega_endereco_id(self, endereco_id):
        endereco_id = self._db_conn.query(Endereco).filter(Endereco.endereco_id == endereco_id).first()
        return endereco_id

    def pega_endereco_pais(self, endereco_id):
        pais_endereco = self._db_conn.query(Endereco.pais_do_usuario).filter(Endereco.endereco_id == endereco_id).first()
        self._db_conn.expunge_all()
        self._db_conn.close()
        return pais_endereco

    def pega_endereco_estado(self, endereco_id):
        estado_endereco = self._db_conn.query(Endereco.estado_do_usuario).filter(Endereco.endereco_id == endereco_id).first()
        self._db_conn.expunge_all()
        self._db_conn.close()
        return estado_endereco

    def pega_endereco_municipio(self, endereco_id):
        municipio_endereco = self._db_conn.query(Endereco.municipio_do_usuario).filter(Endereco.endereco_id == endereco_id).first()
        self._db_conn.expunge_all()
        self._db_conn.close()
        return municipio_endereco

    def pega_endereco_cep(self, endereco_id):
        cep_endereco = self._db_conn.query(Endereco.cep_do_usuario).filter(Endereco.endereco_id == endereco_id).first()
        self._db_conn.expunge_all()
        self._db_conn.close()
        return cep_endereco

    def pega_endereco_rua(self, endereco_id):
        rua_endereco = self._db_conn.query(Endereco.rua_do_usuario).filter(Endereco.endereco_id == endereco_id).first()
        self._db_conn.expunge_all()
        self._db_conn.close()
        return rua_endereco

    def pega_endereco_numero(self, endereco_id):
        numero_endereco = self._db_conn.query(Endereco.numero_da_rua).filter(Endereco.endereco_id == endereco_id).first()
        self._db_conn.expunge_all()
        self._db_conn.close()
        return numero_endereco

    def pega_endereco_complemento(self, endereco_id):
        complemento_endereco = self._db_conn.query(Endereco.complemento).filter(Endereco.endereco_id == endereco_id).first()
        self._db_conn.expunge_all()
        self._db_conn.close()
        return complemento_endereco

    def registra_endereco(self, endereco):
        try:
            self._db_conn.add(endereco)
            self._db_conn.commit()
        except RuntimeError:
            self._db_conn.rollback()
        finally:
            self._db_conn.close()

    def altera_endereco(self, endereco_id, novas_info_endereco):
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

    def deleta_endereco(self, endereco_id):
        self._db_conn.query(Endereco).filter(Endereco.endereco_id == endereco_id).delete()
        self._db_conn.commit()
