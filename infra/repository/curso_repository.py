from infra.entities.curso import Curso
from infra.configs.connection import ConnectionHandler


class CursoRepository:
    # read curso
    def read_curso(self):
        with ConnectionHandler() as conn:
            cursos_dispo = conn.session.query(Curso).filter(Curso.nome.like(f'%%'))
            return cursos_dispo

    # read all
    def select_all(self):
        with ConnectionHandler() as conn:
            cursos = conn.session.query(Curso).all()
            return cursos

    # read one
    def select_one(self, criteiro, busca):
        with ConnectionHandler() as conn:
            if criteiro == 'ID Curso':
                cursos = conn.session.query(Curso).filter(Curso.id.like(f'%{busca}%'))

            elif criteiro == 'Nome':
                cursos = conn.session.query(Curso).filter(Curso.nome.like(f'%{busca}%'))

            elif criteiro == 'Carga Horária':
                cursos = conn.session.query(Curso).filter(Curso.hora.like(f'%{busca}%'))

            elif criteiro == 'Preço R$':
                cursos = conn.session.query(Curso).filter(Curso.preco.like(f'%{busca}%'))

            elif criteiro == 'Tipo':
                cursos = conn.session.query(Curso).filter(Curso.tipo.like(f'%{busca}%'))

            return cursos

    # create
    def insert(self, nome, hora, preco, tipo):
        with ConnectionHandler() as conn:
            curso = Curso(nome=nome, hora=hora, preco=preco, tipo=tipo)
            conn.session.add(curso)
            conn.session.commit()

    # update
    def update(self, id, nome, hora, preco, tipo):
        with ConnectionHandler() as conn:
            curso = conn.session.query(Curso).filter(Curso.id == id).one()

            curso.nome = nome
            curso.hora = hora
            curso.preco = preco
            curso.tipo = tipo

            conn.session.add(curso)
            conn.session.commit()

    # delete
    def delete(self, id):
        with ConnectionHandler() as conn:
            curso = conn.session.query(Curso).filter(Curso.id == id).one()
            conn.session.delete(curso)
            conn.session.commit()