import tkinter as tk
from tkinter import ttk, messagebox
import database.aluno_db as aluno_db
import database.disciplina_db as disciplina_db
import database.nota_db as nota_db
from exportacao import exportar

# ============================================================
# JANELA PRINCIPAL
# ============================================================
def iniciar_gui():
    root = tk.Tk()
    root.title("Sistema de Cadastro de Alunos")
    root.geometry("900x600")

    aba_control = ttk.Notebook(root)
    aba_control.pack(fill="both", expand=True)

    # Criar as abas
    frame_aluno = ttk.Frame(aba_control)
    frame_disciplina = ttk.Frame(aba_control)
    frame_notas = ttk.Frame(aba_control)
    frame_exportar = ttk.Frame(aba_control)

    aba_control.add(frame_aluno, text="Alunos")
    aba_control.add(frame_disciplina, text="Disciplinas")
    aba_control.add(frame_notas, text="Notas")
    aba_control.add(frame_exportar, text="Exportar Dados")

    # Inicializar UIs
    tela_aluno(frame_aluno)
    tela_disciplina(frame_disciplina)
    tela_nota(frame_notas)
    tela_exportar(frame_exportar)

    root.mainloop()


# ============================================================
# ABA ALUNO
# ============================================================
def tela_aluno(frame):
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)

    # -------- FORMULÁRIO --------
    form = ttk.LabelFrame(frame, text="Dados do Aluno")
    form.pack(fill="x", padx=10, pady=10)

    ttk.Label(form, text="Matrícula:").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(form, text="Nome:").grid(row=1, column=0, padx=5, pady=5)
    ttk.Label(form, text="Nascimento:").grid(row=2, column=0, padx=5, pady=5)

    e_matricula = ttk.Entry(form)
    e_nome = ttk.Entry(form)
    e_nascimento = ttk.Entry(form)

    e_matricula.grid(row=0, column=1, padx=5, pady=5)
    e_nome.grid(row=1, column=1, padx=5, pady=5)
    e_nascimento.grid(row=2, column=1, padx=5, pady=5)

    # -------- LISTAGEM --------
    tabela = ttk.Treeview(frame, columns=("mat", "nome", "nasc"), show="headings")
    tabela.heading("mat", text="Matrícula")
    tabela.heading("nome", text="Nome")
    tabela.heading("nasc", text="Nascimento")
    tabela.pack(fill="both", expand=True, padx=10, pady=10)

    def atualizar_lista():
        tabela.delete(*tabela.get_children())
        for a in aluno_db.listar_alunos():
            tabela.insert("", "end", values=a)

    atualizar_lista()

    # -------- BOTÕES --------
    botoes = ttk.Frame(form)
    botoes.grid(row=3, column=0, columnspan=2, pady=10)

    def incluir():
        try:
            aluno_db.inserir_aluno(e_matricula.get(), e_nome.get(), e_nascimento.get())
            atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def alterar():
        try:
            aluno_db.atualizar_aluno(e_matricula.get(), e_nome.get(), e_nascimento.get())
            atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def excluir():
        try:
            aluno_db.excluir_aluno(e_matricula.get())
            atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    ttk.Button(botoes, text="Incluir", command=incluir).grid(row=0, column=0, padx=5)
    ttk.Button(botoes, text="Alterar", command=alterar).grid(row=0, column=1, padx=5)
    ttk.Button(botoes, text="Excluir", command=excluir).grid(row=0, column=2, padx=5)


# ============================================================
# ABA DISCIPLINA
# ============================================================
def tela_disciplina(frame):
    frame.columnconfigure(0, weight=1)

    form = ttk.LabelFrame(frame, text="Dados da Disciplina")
    form.pack(fill="x", padx=10, pady=10)

    labels = ["Nome", "Turno", "Sala", "Professor"]
    entries = []

    for i, lbl in enumerate(labels):
        ttk.Label(form, text=lbl + ":").grid(row=i, column=0, padx=5, pady=5)
        ent = ttk.Entry(form)
        ent.grid(row=i, column=1, padx=5, pady=5)
        entries.append(ent)

    e_nome, e_turno, e_sala, e_professor = entries

    tabela = ttk.Treeview(frame, columns=("id", "nome", "turno", "sala", "prof"), show="headings")
    for col in ("id", "nome", "turno", "sala", "prof"):
        tabela.heading(col, text=col.capitalize())
    tabela.pack(fill="both", expand=True, padx=10, pady=10)

    def atualizar_lista():
        tabela.delete(*tabela.get_children())
        for d in disciplina_db.listar_disciplinas():
            tabela.insert("", "end", values=d)

    atualizar_lista()

    # Selecionar disciplina na tabela
    def selecionar(event):
        item = tabela.focus()
        if not item:
            return
        dados = tabela.item(item)["values"]
        e_nome.delete(0, tk.END); e_nome.insert(0, dados[1])
        e_turno.delete(0, tk.END); e_turno.insert(0, dados[2])
        e_sala.delete(0, tk.END); e_sala.insert(0, dados[3])
        e_professor.delete(0, tk.END); e_professor.insert(0, dados[4])

    tabela.bind("<<TreeviewSelect>>", selecionar)

    # Botões
    botoes = ttk.Frame(form)
    botoes.grid(row=4, column=0, columnspan=2, pady=10)

    def incluir():
        try:
            disciplina_db.inserir_disciplina(e_nome.get(), e_turno.get(), e_sala.get(), e_professor.get())
            atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def alterar():
        item = tabela.focus()
        if not item:
            return messagebox.showwarning("Aviso", "Selecione uma disciplina.")
        id_disc = tabela.item(item)["values"][0]
        try:
            disciplina_db.atualizar_disciplina(id_disc, e_nome.get(), e_turno.get(), e_sala.get(), e_professor.get())
            atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def excluir():
        item = tabela.focus()
        if not item:
            return messagebox.showwarning("Aviso", "Selecione uma disciplina.")
        id_disc = tabela.item(item)["values"][0]
        try:
            disciplina_db.excluir_disciplina(id_disc)
            atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    ttk.Button(botoes, text="Incluir", command=incluir).grid(row=0, column=0, padx=5)
    ttk.Button(botoes, text="Alterar", command=alterar).grid(row=0, column=1, padx=5)
    ttk.Button(botoes, text="Excluir", command=excluir).grid(row=0, column=2, padx=5)


# ============================================================
# ABA NOTAS
# ============================================================
def tela_nota(frame):

    form = ttk.LabelFrame(frame, text="Lançar Nota")
    form.pack(fill="x", padx=10, pady=10)

    ttk.Label(form, text="Matrícula:").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(form, text="ID Disciplina:").grid(row=1, column=0, padx=5, pady=5)
    ttk.Label(form, text="Nota:").grid(row=2, column=0, padx=5, pady=5)

    e_mat = ttk.Entry(form)
    e_disc = ttk.Entry(form)
    e_valor = ttk.Entry(form)

    e_mat.grid(row=0, column=1, padx=5, pady=5)
    e_disc.grid(row=1, column=1, padx=5, pady=5)
    e_valor.grid(row=2, column=1, padx=5, pady=5)

    tabela = ttk.Treeview(frame, columns=("mat", "aluno", "disc", "disc_nome", "valor"), show="headings")
    for col in ("mat", "aluno", "disc", "disc_nome", "valor"):
        tabela.heading(col, text=col.capitalize())
    tabela.pack(fill="both", expand=True, padx=10, pady=10)

    def atualizar_lista():
        tabela.delete(*tabela.get_children())
        for n in nota_db.listar_notas():
            tabela.insert("", "end", values=n)

    atualizar_lista()

    botoes = ttk.Frame(form)
    botoes.grid(row=3, column=0, columnspan=2, pady=10)

    def incluir():
        try:
            nota_db.inserir_nota(e_mat.get(), e_disc.get(), float(e_valor.get()))
            atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def alterar():
        try:
            nota_db.atualizar_nota(e_mat.get(), e_disc.get(), float(e_valor.get()))
            atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def excluir():
        try:
            nota_db.excluir_nota(e_mat.get(), e_disc.get())
            atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    ttk.Button(botoes, text="Incluir", command=incluir).grid(row=0, column=0, padx=5)
    ttk.Button(botoes, text="Alterar", command=alterar).grid(row=0, column=1, padx=5)
    ttk.Button(botoes, text="Excluir", command=excluir).grid(row=0, column=2, padx=5)


# ============================================================
# ABA EXPORTAR
# ============================================================
# ============================================================
# ABA EXPORTAR
# ============================================================
def tela_exportar(frame):

    ttk.Label(frame, text="Exportar dados do sistema", font=("Arial", 14)).pack(pady=20)

    lista_tabelas = ["aluno", "disciplina", "nota"]
    lista_formatos = ["csv", "json", "txt"]

    cb_tabelas = ttk.Combobox(frame, values=lista_tabelas, state="readonly")
    cb_formatos = ttk.Combobox(frame, values=lista_formatos, state="readonly")
    cb_tabelas.pack(pady=5)
    cb_formatos.pack(pady=5)

    def exportar_dados():
        tabela = cb_tabelas.get()
        formato = cb_formatos.get()

        if tabela == "":
            return messagebox.showwarning("Aviso", "Selecione uma tabela.")
        if formato == "":
            return messagebox.showwarning("Aviso", "Selecione um formato.")

        # Chamar a função de listar dados
        if tabela == "aluno":
            dados = aluno_db.listar_alunos()  # Certifique-se de que isso retorna uma lista de listas ou tuplas
        elif tabela == "disciplina":
            dados = disciplina_db.listar_disciplinas()  # Certifique-se de que isso retorna uma lista de listas ou tuplas
        else:
            dados = nota_db.listar_notas()  # Certifique-se de que isso retorna uma lista de listas ou tuplas

        # Verificar se dados não estão vazios
        if not dados:
            return messagebox.showwarning("Aviso", "Não há dados para exportar.")

        # Gerar o nome do arquivo de acordo com a tabela e formato
        nome_arq = f"{tabela}.{formato}"

        try:
            # Chamar a função de exportação (agora usando a função importada de exportacao.py)
            caminho = exportar(dados, nome_arq, formato)
            messagebox.showinfo("OK", f"Arquivo exportado com sucesso:\n{caminho}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao exportar: {e}")

    # Botão para exportar
    ttk.Button(frame, text="Exportar", command=exportar_dados).pack(pady=20)
