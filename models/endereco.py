from models import Base, Column, Integer, String
from sqlalchemy import ForeignKey


class Endereco(Base):
    __tablename__ = 'Endereco'
    endereco_id = Column(Integer, primary_key=True, autoincrement=True)
    fk_id_usuario = Column(Integer, ForeignKey('Usuario.id'))
    pais_do_usuario = Column(String(8), nullable=False)
    estado_do_usuario = Column(String(32), nullable=False)
    municipio_do_usuario = Column(String(64), nullable=False)
    cep_do_usuario = Column(String(9), nullable=False)
    rua_do_usuario = Column(String(64), nullable=False)
    numero_da_rua = Column(Integer, nullable=False)
    complemento = Column(String(64), nullable=False)

    def __init__(self, fk_id_usuario, pais_do_usuario, estado_do_usuario, municipio_do_usuario, cep_do_usuario, rua_do_usuario,
                 numero_da_rua, complemento):
        self.fk_id_usuario = fk_id_usuario
        self.pais_do_usuario = pais_do_usuario
        self.estado_do_usuario = estado_do_usuario
        self.municipio_do_usuario = municipio_do_usuario
        self.cep_do_usuario = cep_do_usuario
        self.rua_do_usuario = rua_do_usuario
        self.numero_da_rua = numero_da_rua
        self.complemento = complemento
