from sqlalchemy import Column, Integer, String

from db.database import Base


class Proprietario(Base):
    __tablename__ = "proprietarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), index=True)
    cpf = Column(String(11), index=True)
    endereco = Column(String(100))
    numero_telefone = Column(String(11))