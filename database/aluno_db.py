from conexao import conectar

# -----------------------------------------------
# CRUD ALUNO
# -----------------------------------------------
def inserir_aluno(matricula, nome, dt_nascimento):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO aluno VALUES (?, ?, ?)", (matricula, nome, dt_nascimento))
    con.commit()
    con.close()


def listar_alunos():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM aluno")
    dados = cur.fetchall()
    con.close()
    return dados


def atualizar_aluno(matricula, nome, dt_nascimento):
    con = conectar()
    cur = con.cursor()
    cur.execute("UPDATE aluno SET nome=?, dt_nascimento=? WHERE matricula=?",
                (nome, dt_nascimento, matricula))
    con.commit()
    con.close()


def excluir_aluno(matricula):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM aluno WHERE matricula=?", (matricula,))
    con.commit()
    con.close()
