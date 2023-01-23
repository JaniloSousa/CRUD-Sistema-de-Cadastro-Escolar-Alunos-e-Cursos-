# fazendo as importações necessárias
# módulos externos
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import Tk

# meus módulos
from infra.repository.aluno_repository import AlunoRepository
from infra.repository.curso_repository import CursoRepository

# minhas cores
azul_titulo = '#7296d1'
vermelho_titulo = '#d17272'
cinza = '#f0f0f0'
verde = '#65eb6c'
vermelho = '#eb6565'
azul_atualizar = '#65cbeb'
azul_pesquisa = '#756e78'


class Janela:
    def __init__(self):
        # criando e configurando minha janela principal
        self.janela = Tk()
        self.janela.iconphoto(False, PhotoImage(file='school_icon.png'))
        self.repo_aluno = AlunoRepository
        self.repo_curso = CursoRepository
        self.janela.geometry('603x700+1250+100')
        self.janela.title('Sistema Escolar')
        #self.janela.resizable(False, False)
        self.matricula = None
        self.id = None

        self.criador = Label(self.janela, text='Created by Janilo Sousa', font=('Ivy 7 italic'))
        self.criador.place(x=250, y=682)

        # definindo um estilo para a minha janela principal
        self.style = ttk.Style(self.janela)
        self.style.theme_use('clam')

        # meu notbook
        self.notbook = ttk.Notebook(self.janela)
        self.notbook.place(x=0, y=0)

        # aba dos alunos
        self.aba_alunos =Frame(self.notbook)
        self.notbook.add(self.aba_alunos, text='Alunos')

        # aba dos cursos
        self.aba_cursos=Frame(self.notbook)
        self.notbook.add(self.aba_cursos, text='Cursos')

        # FRONT-END ABA ALUNOS
        # FRAME TITULO -----------------------------------------------------------------------
        # frame
        self.frame_titulo = Frame(self.aba_alunos, width=600, height=110, bg=azul_titulo)
        self.frame_titulo.grid(row=0, column=0, columnspan=2)

        # label
        self.lb_titulo = Label(self.frame_titulo, text='CADASTRO DE ALUNOS', fg='white', bg=azul_titulo, font=('Arial 25 bold'))
        self.lb_titulo.place(x=10, y=30)

        # imagem do aluno
        self.aluno_icon = Image.open('aluno_icon.png')
        self.aluno_icon = self.aluno_icon.resize((90, 90))
        self.aluno_icon = ImageTk.PhotoImage(self.aluno_icon)

        # label da imagem
        self.lb_aluno_icon = Label(self.frame_titulo, image=self.aluno_icon, bg=azul_titulo)
        self.lb_aluno_icon.place(x=450, y=5)

        # label da linha
        self.lb_linha = Label(self.frame_titulo, text='', font=('Ivy 1 bold'), width=600, height=1, bg='#756e78')
        self.lb_linha.place(x=0, y=102)

        # FRAME DOS DADOS --------------------------------------------------------------------------
        # frame
        self.frame_campos = LabelFrame(self.aba_alunos, text='Dados Do Aluno(a)', width=300, height=280, font=('Ivy 9 bold'))
        self.frame_campos.grid(row=1, column=0, rowspan=2)

        # NOME ----------------------------
        # label
        self.lb_nome = Label(self.frame_campos, text='Nome: ', font=('Ivy 10'))
        self.lb_nome.place(x=10, y=10)

        # entry
        self.ent_nome_aluno = Entry(self.frame_campos, width=35)
        self.ent_nome_aluno.place(x=75, y=10)

        # label erro
        self.lb_erro_nome_aluno = Label(self.frame_campos, text='Entre com um nome válido', fg=cinza, font=('Ivy 8 italic'))
        self.lb_erro_nome_aluno.place(x=75, y=35)

        # IDADE ----------------------------
        # label
        self.lb_idade = Label(self.frame_campos, text='Idade: ', font=('Ivy 10'))
        self.lb_idade.place(x=10, y=60)

        # spin box
        self.sb_idade=Spinbox(self.frame_campos, from_=10, to=100, width=6)
        self.sb_idade.place(x=75, y=60)

        # label erro
        self.lb_erro_idade = Label(self.frame_campos, text='Entre com uma idade válida', fg=cinza, font=('Ivy 8 italic'))
        self.lb_erro_idade.place(x=75, y=85)

        # CURSO ----------------------------
        # label
        self.lb_curso = Label(self.frame_campos, text='Curso: ', font=('Ivy 10'))
        self.lb_curso.place(x=10, y=110)

        # combo box
        self.lista_cursos_dispo =[]
        self.cb_cursos=ttk.Combobox(self.frame_campos, values=self.lista_cursos_dispo)
        self.cb_cursos.set('') # valor padrão
        self.cb_cursos.place(x=75, y=110)

        # label erro
        self.lb_erro_curso = Label(self.frame_campos, text='Escolha um dos nossos cursos', fg=cinza, font=('Ivy 8 italic'))
        self.lb_erro_curso.place(x=75, y=135)

        # NOTA ----------------------------
        # label
        self.lb_nota = Label(self.frame_campos, text='Nota: ', font=('Ivy 10'))
        self.lb_nota.place(x=10, y=160)

        # entry
        self.ent_nota = Entry(self.frame_campos, width=7)
        self.ent_nota.place(x=75, y=160)

        # label erro
        self.lb_erro_nota = Label(self.frame_campos, text='Entre com uma nota válida', fg=cinza, font=('Ivy 8 italic'))
        self.lb_erro_nota.place(x=75, y=185)

        # PREMIUM ----------------------------
        # label
        self.lb_premium = Label(self.frame_campos, text='Premium: ', font=('Ivy 10'))
        self.lb_premium.place(x=10, y=210)

        # combo box
        self.lista_premium = ['Sim', 'Não']
        self.cb_premium = ttk.Combobox(self.frame_campos, values=self.lista_premium, width=5)
        self.cb_premium.set('')
        self.cb_premium.place(x=75, y=210)

        # label erro
        self.lb_erro_premium = Label(self.frame_campos, text='Entre com ou SIM ou NÃO', fg=cinza, font=('Ivy 8 italic'))
        self.lb_erro_premium.place(x=75, y=235)

        # imagem da borracha
        self.eraser_icon = Image.open('eraser.png')
        self.eraser_icon = self.eraser_icon.resize((15, 15))
        self.eraser_icon = ImageTk.PhotoImage(self.eraser_icon)


        # botão de limpar campos dos alunos
        self.bnt_limpar_campos_alunos = Button(self.frame_campos, text='', image=self.eraser_icon, compound=RIGHT, bg=azul_pesquisa, font=('Ivy 10 bold'), fg='white', command=self.limparCampos)
        self.bnt_limpar_campos_alunos.place(x=265, y=212)

        # FRAME PESQUISA -------------------------------------------------------------------------
        # frame
        self.frame_pesquisa = LabelFrame(self.aba_alunos, text='Consultas', width=300, height=140, font=('Ivy 9 bold'))
        self.frame_pesquisa.grid(row=1, column=1)

        # label
        self.lb_pesquisa = Label(self.frame_pesquisa, text='Pesquisar por: ',font=('Ivy 9'))
        self.lb_pesquisa.place(x=10, y=17)

        # combo box
        self.lista_pesquisa = ['Matrícula', 'Nome', 'Idade', 'Curso', 'Nota', 'Premium']
        self.cb_pesquisa=ttk.Combobox(self.frame_pesquisa, values=self.lista_pesquisa, width=26)
        self.cb_pesquisa.set('Nome')
        self.cb_pesquisa.place(x=105, y=17)

        # entry
        self.ent_pesquisa = Entry(self.frame_pesquisa, width=45)
        self.ent_pesquisa.place(x=10, y=45)

        # imagem da lupa
        self.lupa_icon = Image.open('lupa_icon.png')
        self.lupa_icon = self.lupa_icon.resize((20, 20))
        self.lupa_icon = ImageTk.PhotoImage(self.lupa_icon)

        # button
        self.bnt_pesquisa = Button(self.frame_pesquisa, command=self.pesquisar, image=self.lupa_icon, compound=RIGHT, text='Pesquisar  ', width=160, font=('Ivy 10 bold'), bg=azul_pesquisa, fg='white')
        self.bnt_pesquisa.place(x=60, y=70)

        # FRAME ACÕES --------------------------------------------------------------------------------------
        # frame
        self.frame_acoes = LabelFrame(self.aba_alunos, text='Ações', width=300, height=140, font=('Ivy 9 bold'))
        self.frame_acoes.grid(row=2, column=1)

        # botão criar
        self.bnt_create = Button(self.frame_acoes, command=self.cadastrar, text='Cadastrar', width=22, bg=verde, fg='white', font=('Ivy 10 bold'))
        self.bnt_create.place(x=60, y=25)

        # botão atualizar
        self.bnt_update = Button(self.frame_acoes, command=self.atualizar, text='Atualizar', width=10, fg='white', bg=azul_atualizar, font=('Ivy 10 bold'))
        self.bnt_update.place(x=60, y=55)

        # botão excluir
        self.bnt_delete = Button(self.frame_acoes, command=self.excluir, text='Excluir', width=10, fg='white', bg=vermelho, font=('Ivy 10 bold'))
        self.bnt_delete.place(x=155, y=55)

        # FRAME TABELA ------------------------------------------------------------------------------------
        # frame
        self.frame_tabela = LabelFrame(self.aba_alunos, text='Tabela', width=603, height=285, font=('Ivy 9 bold'))
        self.frame_tabela.grid(row=3, column=0, columnspan=2)

        # criando minha tabela
        self.colunas = ['matricula', 'nome', 'idade', 'curso', 'nota', 'premium']
        self.tabela = ttk.Treeview(self.frame_tabela, selectmode='extended', columns = self.colunas, show='headings')
        self.tabela.grid(column=0, row=0, sticky='nsew')

        # criando meus scrool bar
        self.vsb = ttk.Scrollbar(self.frame_tabela, orient='vertical', command=self.tabela.yview)
        self.vsb.grid(column=1, row=0, sticky='ns')

        self.hsb = ttk.Scrollbar(self.frame_tabela, orient='horizontal', command=self.tabela.xview)
        self.hsb.grid(column=0, row=1, sticky='ew')

        # associando meus scrool bar com minha tablea
        self.tabela.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

        # evento do usuário clicar em uma linha da tebela
        self.tabela.bind('<ButtonRelease-1>', self.capturarDados)

        # definindo um nome para as minhas colunas
        self.tabela.heading(0, text='Matrícula', anchor='nw')
        self.tabela.heading(1, text='Nome', anchor='nw')
        self.tabela.heading(2, text='Idade', anchor='nw')
        self.tabela.heading(3, text='Curso', anchor='nw')
        self.tabela.heading(4, text='Nota', anchor='nw')
        self.tabela.heading(5, text='Premium', anchor='nw')

        # definindo a largura das minhas colunas
        self.tabela.column(0, width=65, anchor='nw')
        self.tabela.column(1, width=185, anchor='nw')
        self.tabela.column(2, width=45, anchor='nw')
        self.tabela.column(3, width=170, anchor='nw')
        self.tabela.column(4, width=45, anchor='nw')
        self.tabela.column(5, width=65, anchor='nw')

        self.preencherTv()

        # FRONT-END DA ABA CURSOS
        # FRAME TITULO -----------------------------------------------------------------------
        # frame
        self.frame_titulo = Frame(self.aba_cursos, width=600, height=110, bg=vermelho_titulo)
        self.frame_titulo.grid(row=0, column=0, columnspan=2)

        # label
        self.lb_titulo = Label(self.frame_titulo, text='CADASTRO DE CURSOS', fg='white', bg=vermelho_titulo,
                               font=('Arial 25 bold'))
        self.lb_titulo.place(x=10, y=30)

        # imagem do aluno
        self.books_icon = Image.open('books_icon.png')
        self.books_icon = self.books_icon.resize((100, 90))
        self.books_icon = ImageTk.PhotoImage(self.books_icon)

        # label da imagem
        self.lb_books_icon = Label(self.frame_titulo, image=self.books_icon, bg=vermelho_titulo)
        self.lb_books_icon.place(x=450, y=5)

        # label da linha
        self.lb_linha = Label(self.frame_titulo, text='', font=('Ivy 1 bold'), width=600, height=1, bg='#756e78')
        self.lb_linha.place(x=0, y=102)

        # FRAME DOS DADOS --------------------------------------------------------------------------
        # frame
        self.frame_campos = LabelFrame(self.aba_cursos, text='Dados Do Curso', width=300, height=280, font=('Ivy 9 bold'))
        self.frame_campos.grid(row=1, column=0, rowspan=2)

        # NOME DO CURSO ----------------------------
        # label
        self.lb_nome = Label(self.frame_campos, text='Nome: ', font=('Ivy 10'))
        self.lb_nome.place(x=10, y=10)

        # entry
        self.ent_nome_curso = Entry(self.frame_campos, width=33)
        self.ent_nome_curso.place(x=85, y=10)

        # label erro
        self.lb_erro_nome_curso = Label(self.frame_campos, text='Não pode ficar vazio', fg=cinza,
                                  font=('Ivy 8 italic'))
        self.lb_erro_nome_curso.place(x=85, y=35)

        # CARGA HORÁRIA ----------------------------
        # label
        self.lb_hora = Label(self.frame_campos, text='Carga\nHorária: ', font=('Ivy 10'), justify=LEFT)
        self.lb_hora.place(x=10, y=60)

        # spin box
        self.sb_hora = Spinbox(self.frame_campos, from_=20, to=40, width=6)
        self.sb_hora.place(x=85, y=70)

        # label erro
        self.lb_erro_hora = Label(self.frame_campos, text='Entre com uma carga\nhorária válida', fg=cinza,
                                  font=('Ivy 8 italic'))
        self.lb_erro_hora.place(x=145, y=63)

        # PREÇO ----------------------------
        # label
        self.lb_preco = Label(self.frame_campos, text='Preço R$: ', font=('Ivy 10'))
        self.lb_preco.place(x=10, y=110)

        # entry
        self.ent_preco = Entry(self.frame_campos, width=7)
        self.ent_preco.place(x=85, y=110)

        # label erro
        self.lb_erro_preco = Label(self.frame_campos, text='Entre com um preço válido', fg=cinza,
                                   font=('Ivy 8 italic'))
        self.lb_erro_preco.place(x=85, y=135)

        # PRESENCIAL ----------------------------
        # label
        self.lb_presencial = Label(self.frame_campos, text='Tipo: ', font=('Ivy 10'))
        self.lb_presencial.place(x=10, y=160)

        # combo box
        self.lista_presencial = ['Presencial', 'Online']
        self.cb_presencial = ttk.Combobox(self.frame_campos, values=self.lista_presencial, width=10)
        self.cb_presencial.set('')
        self.cb_presencial.place(x=85, y=160)

        # label erro
        self.lb_erro_presencial = Label(self.frame_campos, text='Entre com ou Presencial ou Online', fg=cinza,
                                        font=('Ivy 8 italic'))
        self.lb_erro_presencial.place(x=85, y=185)

        # botão de limpar campos dos alunos
        self.bnt_limpar_campos_cursos = Button(self.frame_campos, text='', image=self.eraser_icon, compound=RIGHT,
                                               bg=azul_pesquisa, font=('Ivy 10 bold'), fg='white',
                                               command=self.limparCamposCurso)
        self.bnt_limpar_campos_cursos.place(x=265, y=160)

        # FRAME PESQUISA -------------------------------------------------------------------------
        # frame
        self.frame_pesquisa = LabelFrame(self.aba_cursos, text='Consultas', width=300, height=140, font=('Ivy 9 bold'))
        self.frame_pesquisa.grid(row=1, column=1)

        # label
        self.lb_pesquisa = Label(self.frame_pesquisa, text='Pesquisar por: ', font=('Ivy 9'))
        self.lb_pesquisa.place(x=10, y=17)

        # combo box
        self.lista_pesquisa_cursos = ['ID Curso', 'Nome', 'Carga Horária', 'Preço R$', 'Tipo']
        self.cb_pesquisa_cursos = ttk.Combobox(self.frame_pesquisa, values=self.lista_pesquisa_cursos, width=26)
        self.cb_pesquisa_cursos.set('Nome')
        self.cb_pesquisa_cursos.place(x=105, y=17)

        # entry
        self.ent_pesquisa_cursos = Entry(self.frame_pesquisa, width=45)
        self.ent_pesquisa_cursos.place(x=10, y=45)

        # imagem da lupa
        self.lupa_icon_cursos = Image.open('lupa_icon.png')
        self.lupa_icon_cursos = self.lupa_icon_cursos.resize((20, 20))
        self.lupa_icon_cursos = ImageTk.PhotoImage(self.lupa_icon_cursos)

        # button
        self.bnt_pesquisa_curso = Button(self.frame_pesquisa, command=self.pesquisarCurso, image=self.lupa_icon_cursos,
                                   compound=RIGHT,
                                   text='Pesquisar  ', width=160, font=('Ivy 10 bold'), bg=azul_pesquisa, fg='white')
        self.bnt_pesquisa_curso.place(x=60, y=70)

        # FRAME ACÕES --------------------------------------------------------------------------------------
        # frame
        self.frame_acoes = LabelFrame(self.aba_cursos, text='Ações', width=300, height=140, font=('Ivy 9 bold'))
        self.frame_acoes.grid(row=2, column=1)

        # botão criar
        self.bnt_create = Button(self.frame_acoes, command=self.cadastrarCurso, text='Cadastrar', width=22, bg=verde,
                                 fg='white',
                                 font=('Ivy 10 bold'))
        self.bnt_create.place(x=60, y=25)

        # botão atualizar
        self.bnt_update = Button(self.frame_acoes, command=self.atualizarCurso, text='Atualizar', width=10, fg='white',
                                 bg=azul_atualizar, font=('Ivy 10 bold'))
        self.bnt_update.place(x=60, y=55)

        # botão excluir
        self.bnt_delete = Button(self.frame_acoes, command=self.excluirCurso, text='Excluir', width=10, fg='white',
                                 bg=vermelho, font=('Ivy 10 bold'))
        self.bnt_delete.place(x=155, y=55)

        # FRAME TABELA ------------------------------------------------------------------------------------
        # frame
        self.frame_tabela = LabelFrame(self.aba_cursos, text='Tabela', width=603, height=285, font=('Ivy 9 bold'))
        self.frame_tabela.grid(row=3, column=0, columnspan=2)

        # criando minha tabela
        self.colunas_cursos = ['id curso', 'nome', 'hora', 'preco', 'tipo']
        self.tabela_cursos = ttk.Treeview(self.frame_tabela, selectmode='extended', columns=self.colunas_cursos,
                                          show='headings')
        self.tabela_cursos.grid(column=0, row=0, sticky='nsew')

        # criando meus scrool bar
        self.vsb = ttk.Scrollbar(self.frame_tabela, orient='vertical', command=self.tabela_cursos.yview)
        self.vsb.grid(column=1, row=0, sticky='ns')

        self.hsb = ttk.Scrollbar(self.frame_tabela, orient='horizontal', command=self.tabela_cursos.xview)
        self.hsb.grid(column=0, row=1, sticky='ew')

        # associando meus scrool bar com minha tablea
        self.tabela_cursos.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

        # evento do usuário clicar em uma linha da tebela
        self.tabela_cursos.bind('<ButtonRelease-1>', self.capturarDadosCurso)

        # definindo um nome para as minhas colunas
        self.tabela_cursos.heading(0, text='ID Curso', anchor='nw')
        self.tabela_cursos.heading(1, text='Nome', anchor='nw')
        self.tabela_cursos.heading(2, text='Qtd. Horas', anchor='nw')
        self.tabela_cursos.heading(3, text='Preço R$', anchor='nw')
        self.tabela_cursos.heading(4, text='Tipo', anchor='nw')

        # definindo a largura das minhas colunas
        self.tabela_cursos.column(0, width=65, anchor='nw')
        self.tabela_cursos.column(1, width=285, anchor='nw')
        self.tabela_cursos.column(2, width=75, anchor='nw')
        self.tabela_cursos.column(3, width=65, anchor='nw')
        self.tabela_cursos.column(4, width=85, anchor='nw')

        self.preencherTvCurso()
        self.janela.mainloop()


    # BACK-END DA ABA ALUNO
    def limparErrosAluno(self):
        # resetando as mensagens de erro
        self.lb_erro_nome_aluno['fg'] = cinza
        self.lb_erro_idade['fg'] = cinza
        self.lb_erro_curso['fg'] = cinza
        self.lb_erro_nota['fg'] = cinza
        self.lb_erro_premium['fg'] = cinza

    def validarDadosAluno(self):
        self.limparErrosAluno()
        num = 0
        # validando o nome
        y = self.ent_nome_aluno.get().replace(' ', '')
        if self.ent_nome_aluno != '' and (y.isalpha()):
            num += 1
        else:
            self.lb_erro_nome_aluno['fg'] = vermelho

        # validando a idade
        if self.sb_idade != '' and (self.sb_idade.get()).isnumeric():
            num += 1
        else:
            self.lb_erro_idade['fg'] = vermelho

        # validando o curso
        if self.ent_nome_curso != '' and ((self.cb_cursos.get()) in self.lista_cursos_dispo):
            num += 1
        else:
            self.lb_erro_curso['fg'] = vermelho

        # validando a nota
        x = self.ent_nota.get().replace('.', '')
        if self.ent_nota != '' and (x.isnumeric()):
            num += 1
        else:
            self.lb_erro_nota['fg'] = vermelho

        # validando se o aluno é premium ou não
        if self.cb_premium.get() != '' and (self.cb_premium.get() in ['Sim', 'Não']):
            num += 1
        else:
            self.lb_erro_premium['fg'] = vermelho

        return num


    # função que atualiza a lista com os cursos disponíveis
    def buscarCursos(self):
        cursos_dispo = self.repo_curso.read_curso(self)
        self.lista_cursos_dispo.clear()
        for curso in cursos_dispo:
            self.lista_cursos_dispo.append(curso.nome)

        self.cb_cursos['values'] = self.lista_cursos_dispo

    def pesquisar(self):
        self.buscarCursos()
        criterio = self.cb_pesquisa.get()
        busca = self.ent_pesquisa.get()
        alunos = self.repo_aluno.select_one(self, criterio, busca)

        self.esvaziarTv()
        for aluno in alunos:
            self.tabela.insert("", "end", values=(aluno.matricula, aluno.nome, aluno.idade, aluno.curso, aluno.nota, aluno.premium))

    def preencherTv(self):
        alunos = self.repo_aluno.select_all(self)

        self.esvaziarTv()
        for aluno in alunos:
            self.tabela.insert("", "end", values=(
            aluno.matricula, aluno.nome, aluno.idade, aluno.curso, aluno.nota, aluno.premium))
        self.buscarCursos()

    def esvaziarTv(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

    def limparCampos(self):
        self.ent_nome_aluno.delete(0, "end")

        self.sb_idade.delete(0, 'end')
        self.sb_idade.insert(0, 10)

        self.cb_cursos.set("")
        self.ent_nota.delete(0, "end")
        self.cb_premium.set('')

    def cadastrar(self):
        ok = self.validarDadosAluno()
        if ok == 5:
            nome = self.ent_nome_aluno.get()
            idade = int(self.sb_idade.get())
            curso = self.cb_cursos.get()
            nota = float(self.ent_nota.get())
            premium = self.cb_premium.get()

            self.repo_aluno.insert(self, nome, idade, curso, nota, premium)
            self.limparCampos()
            self.esvaziarTv()
            self.preencherTv()

    def capturarDados(self, event):
        self.limparErrosAluno()
        self.limparCampos()
        selecionado = self.tabela.selection()[0]
        aluno = self.tabela.item(selecionado, "values")

        self.matricula = aluno[0]

        # PREENCHENDO OS CAMPOS -----------------------------------
        self.ent_nome_aluno.insert(0, aluno[1])
        self.sb_idade.delete(0, 'end')
        self.sb_idade.insert(0, aluno[2])
        self.cb_cursos.set(aluno[3])
        self.ent_nota.insert(0, aluno[4])
        self.cb_premium.set(aluno[5])

    def excluir(self):
        msb = messagebox.askyesno('Tem Certeza?', 'Tem certeza que deseja excluir esse registro?')
        if msb == True:
            self.repo_aluno.delete(self, self.matricula)
            self.limparCampos()
            self.esvaziarTv()
            self.preencherTv()
            messagebox.showinfo('Sucesso', 'Registro excluído com sucesso!')


    def atualizar(self):
        ok = self.validarDadosAluno()
        if ok == 5:
            msb = messagebox.askyesno('Tem Certeza?', 'Tem certeza que deseja atualizar esse registro?')
            if msb == True:
                nome = self.ent_nome_aluno.get()
                idade = int(self.sb_idade.get())
                curso = self.cb_cursos.get()
                nota = float(self.ent_nota.get())
                premium = self.cb_premium.get()

                self.repo_aluno.update(self, self.matricula, nome, idade, curso, nota, premium)

                self.limparCampos()
                self.esvaziarTv()
                self.preencherTv()
                messagebox.showinfo('Sucesso', 'Registro atualizado com sucesso!')



    # BACK-END DA ABA CURSOS
    def limparErrosCurso(self):
        self.lb_erro_presencial['fg'] = cinza
        self.lb_erro_preco['fg'] = cinza
        self.lb_erro_hora['fg'] = cinza
        self.lb_erro_nome_curso['fg'] = cinza

    def validarCurso(self):
        self.limparErrosCurso()
        ok = 0
        # validando o tipo do curso (ou presencial ou online)
        if self.cb_presencial.get() != '' and ((self.cb_presencial.get()) in ['Presencial', 'Online']):
            ok += 1
        else:
            self.lb_erro_presencial['fg'] = vermelho

        # validando o preço
        a = self.ent_preco.get().replace('.', '')
        if self.ent_preco.get() != '' and (a.isnumeric()):
            ok += 1
        else:
            self.lb_erro_preco['fg'] = vermelho

        # validando a carga horaria
        if self.sb_hora.get() and ((self.sb_hora.get()).isnumeric()):
            ok += 1
        else:
            self.lb_erro_hora['fg'] = vermelho

        # validando o nome do curso(não pode tá vazio)
        if self.ent_nome_curso.get() != '':
            ok += 1
        else:
            self.lb_erro_nome_curso['fg'] = vermelho

        return ok


    def pesquisarCurso(self):
        self.buscarCursos()
        criterio = self.cb_pesquisa_cursos.get()
        busca = self.ent_pesquisa_cursos.get()
        cursos = self.repo_curso.select_one(self, criterio, busca)

        self.esvaziarTvCurso()
        for curso in cursos:
            self.tabela_cursos.insert("", "end", values=(curso.id, curso.nome, curso.hora, curso.preco, curso.tipo))

    def preencherTvCurso(self):
        cursos = self.repo_curso.select_all(self)

        self.esvaziarTvCurso()
        for curso in cursos:
            self.tabela_cursos.insert("", "end", values=(curso.id, curso.nome, curso.hora, curso.preco, curso.tipo))
        self.buscarCursos()

    def esvaziarTvCurso(self):
        for item in self.tabela_cursos.get_children():
            self.tabela_cursos.delete(item)


    def limparCamposCurso(self):
        self.ent_nome_curso.delete(0, "end")

        self.sb_hora.delete(0, 'end')
        self.sb_hora.insert(0, 20)

        self.ent_preco.delete(0, 'end')

        self.ent_nota.delete(0, "end")
        self.cb_presencial.set('')


    def cadastrarCurso(self):
        ok = self.validarCurso()
        if ok == 4:
            nome = self.ent_nome_curso.get()
            hora = int(self.sb_hora.get())
            preco = self.ent_preco.get()
            tipo = self.cb_presencial.get()


            self.repo_curso.insert(self, nome, hora, preco, tipo)
            self.limparCamposCurso()
            self.esvaziarTvCurso()
            self.preencherTvCurso()

    def capturarDadosCurso(self, event):
        self.limparErrosCurso()
        self.limparCamposCurso()
        selecionado = self.tabela_cursos.selection()[0]
        curso = self.tabela_cursos.item(selecionado, "values")

        self.id = curso[0] # id do curso

        # PREENCHENDO OS CAMPOS -----------------------------------
        self.ent_nome_curso.insert(0, curso[1]) # nome do curso
        self.sb_hora.delete(0, 'end') # limpando o spin box
        self.sb_hora.insert(0, curso[2]) # carga horária do curso
        self.ent_preco.insert(0, curso[3]) # preço do curso
        self.cb_presencial.set(curso[4]) # tipo do curso


    def excluirCurso(self):
        msb = messagebox.askyesno('Tem certeza? ', 'Tem certeza que deseja excluir esse registro?')
        if msb == True:
            self.repo_curso.delete(self, self.id)
            self.limparCamposCurso()
            self.esvaziarTvCurso()
            self.preencherTvCurso()
            messagebox.showinfo('Sucesso', 'Registro excluído com sucesso!')

    def atualizarCurso(self):
        ok = self.validarCurso()
        if ok == 4:
            msb = messagebox.askyesno('Tem certeza?', 'Tem certeza que deseja atualizar esse registro?')
            if msb == True:
                curso = self.ent_nome_curso.get()
                hora = int(self.sb_hora.get())
                preco = self.ent_preco.get()
                tipo = self.cb_presencial.get()

                self.repo_curso.update(self, self.id, curso, hora, preco, tipo)

                self.limparCamposCurso()
                self.esvaziarTvCurso()
                self.preencherTvCurso()
                messagebox.showinfo('Sucesso', 'Registro atualizado com sucesso!')


# minha tela de login
tela_login = Tk()
tela_login.geometry('252x252')
tela_login.resizable(False, False)
tela_login.title('Sistema Escolar')
tela_login.iconphoto(False, PhotoImage(file='school_icon.png'))

# função que pega o usuário e a senha e confere
def fazerLogin():
    lb_erro['fg'] = cinza
    usuario = ent_uso.get()
    senha = ent_senha.get()
    if usuario == 'janilo' and senha == '123':
        tela_login.destroy()
        Janela()
    else:
        lb_erro['fg'] = vermelho

# frame da tela de login
frame_login = LabelFrame(tela_login, text='Tela De Login', width=250, height=250, relief='solid', font=('Ivy 10 bold'))
frame_login.grid(row=0, column=0)

# imagem da escola
icon_school_login = Image.open('school_login_icon.png')
icon_school_login = icon_school_login.resize((90, 90))
icon_school_login = ImageTk.PhotoImage(icon_school_login)

# label da imagem
lb_imagem = Label(frame_login, image=icon_school_login)
lb_imagem.place(x=75, y=10)

# label + entry (usuário)
lb_uso = Label(frame_login, text='Usuário: ', font=('Ivy 10 bold'))
lb_uso.place(x=20, y=120)
ent_uso = Entry(frame_login)
ent_uso.place(x=90, y=120)

# label + entry (senha)
lb_senha = Label(frame_login, text='Senha: ', font=('Ivy 10 bold'))
lb_senha.place(x=20, y=145)
ent_senha = Entry(frame_login, show='•')
ent_senha.place(x=90, y=145)

# label do erro
lb_erro = Label(frame_login, text='Senha ou usuário incorreto', font=('Ivy 7 italic'), fg=cinza)
lb_erro.place(x=90, y=170)

# botão para entrar
bnt_login = Button(frame_login, text='Entrar', width=15, bg='#c52727', font=('Ivy 10 bold'), fg='white', command=fazerLogin)
bnt_login.place(x=60, y=190)


tela_login.mainloop()