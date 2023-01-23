from sqlalchemy import Column, Integer, String, Float
from infra.configs.base import Base


class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    hora = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)
    tipo = Column(String(10), nullable=False)