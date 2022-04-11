from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql+pymysql://root:password@localhost:3306/ProjetoPT', echo=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         expire_on_commit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models.usuario import Usuario
    from models.endereco import Endereco
    Base.metadata.create_all(bind=engine, tables=[Usuario.__table__, Endereco.__table__])


if __name__ == '__main__':
    init_db()
