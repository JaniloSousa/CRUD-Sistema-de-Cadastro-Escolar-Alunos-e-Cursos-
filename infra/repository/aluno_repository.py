from infra.entities.aluno import Aluno
from infra.configs.connection import ConnectionHandler


class AlunoRepository:
    # read all
    def select_all(self):
        with ConnectionHandler() as conn:
            alunos = conn.session.query(Aluno).all()
            return alunos

    # read one
    def select_one(self, criteiro, busca):
        with ConnectionHandler() as conn:
            if criteiro == 'Matrícula':
                alunos = conn.session.query(Aluno).filter(Aluno.matricula.like(f'%{busca}%'))

            elif criteiro == 'Nome':
                alunos = conn.session.query(Aluno).filter(Aluno.nome.like(f'%{busca}%'))

            elif criteiro == 'Idade':
                alunos = conn.session.query(Aluno).filter(Aluno.idade.like(f'%{busca}%'))

            elif criteiro == 'Curso':
                alunos = conn.session.query(Aluno).filter(Aluno.curso.like(f'%{busca}%'))

            elif criteiro == 'Nota':
                alunos = conn.session.query(Aluno).filter(Aluno.nota.like(f'%{busca}%'))

            elif criteiro == 'Premium':
                alunos = conn.session.query(Aluno).filter(Aluno.premium.like(f'%{busca}%'))

            return alunos

    # create
    def insert(self, nome, idade, curso, nota, premium):
        with ConnectionHandler() as conn:
            aluno = Aluno(nome=nome, idade=idade, curso=curso, nota=nota, premium=premium)
            conn.session.add(aluno)
            conn.session.commit()

    # update
    def update(self, matricula, nome, idade, curso, nota, premium):
        with ConnectionHandler() as conn:
            aluno = conn.session.query(Aluno).filter(Aluno.matricula == matricula).one()

            aluno.nome = nome
            aluno.idade = idade
            aluno.curso = curso
            aluno.nota = nota
            aluno.premium = premium

            conn.session.add(aluno)
            conn.session.commit()

    # delete
    def delete(self, matricula):
        with ConnectionHandler() as conn:
            aluno = conn.session.query(Aluno).filter(Aluno.matricula == matricula).one()
            conn.session.delete(aluno)
            conn.session.commit()