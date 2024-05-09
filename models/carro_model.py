from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class Carro(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    modelo = Column(String(50), index=True)
    placa = Column(String(7), index=True)
    cor = Column(String(20))
    proprietario_id = Column(Integer, ForeignKey("proprietarios.id"), nullable=False)
    proprietario = relationship("Proprietario")