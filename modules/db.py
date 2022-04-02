from flask_login import UserMixin
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

engine = create_engine('mysql+pymysql://root:password@localhost:3306/ProjetoPT', echo=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         expire_on_commit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Usuario(Base, UserMixin):
    __tablename__ = 'Usuario'
    usuario_id = Column(Integer, primary_key=True, autoincrement=True)
    nome_do_usuario = Column(String(26), nullable=False)
    email_do_usuario = Column(String(64), nullable=False, unique=True)
    senha_do_usuario = Column(String(256), nullable=False)
    cpf_do_usuario = Column(String(12), nullable=False, unique=True)
    pis_do_usuario = Column(String(12), nullable=False, unique=True)

    endereco_usuario = relationship('Endereco', backref=backref('Usuario'))

    def __init__(self, nome_do_usuario, email_do_usuario, senha_do_usuario, cpf_do_usuario, pis_do_usuario):
        self.nome_do_usuario = nome_do_usuario
        self.email_do_usuario = email_do_usuario
        self.senha_do_usuario = senha_do_usuario
        self.cpf_do_usuario = cpf_do_usuario
        self.pis_do_usuario = pis_do_usuario


@property
def is_authenticated(self):
    return True


@property
def is_active(self):
    return True


@property
def is_anonymous(self):
    return False


class Endereco(Base):
    __tablename__ = 'Endereco'
    endereco_id = Column(Integer, primary_key=True, autoincrement=True)
    fk_id_usuario = Column(Integer, ForeignKey('Usuario.usuario_id'))
    pais_do_usuario = Column(String(8), nullable=False)
    estado_do_usuario = Column(String(32), nullable=False)
    municipio_do_usuario = Column(String(64), nullable=False)
    cep_do_usuario = Column(Integer, nullable=False)
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


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
