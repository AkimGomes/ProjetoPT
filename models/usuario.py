from flask_login import UserMixin
from models import Base, Column, Integer, String, relationship, backref
from sqlalchemy.schema import Table


class Usuario(Base, UserMixin):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_do_usuario = Column(String(26), nullable=False)
    email_do_usuario = Column(String(64), nullable=False, unique=True)
    senha_do_usuario = Column(String(256), nullable=False)
    cpf_do_usuario = Column(String(14), nullable=False, unique=True)
    pis_do_usuario = Column(String(14), nullable=False, unique=True)

    endereco_usuario = relationship('Endereco', backref=backref('Usuario'), cascade='all, delete', passive_deletes=True)

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


@property
def get_id(self):
    return self.id
