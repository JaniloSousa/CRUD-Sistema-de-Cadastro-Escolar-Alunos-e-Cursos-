from sqlalchemy import Column, Integer, String, Float
from infra.configs.base import Base


class Aluno(Base):
    __tablename__ = 'aluno'
    matricula = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60), nullable=False)
    idade = Column(Integer, nullable=False)
    curso = Column(String(60), nullable=False)
    nota = Column(Float, nullable=False)
    premium = Column(String(5), nullable=False)