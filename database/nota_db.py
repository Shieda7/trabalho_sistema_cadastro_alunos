from conexao import conectar

# -----------------------------------------------
# CRUD NOTA
# -----------------------------------------------
def inserir_nota(matricula, disciplina_id, valor):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO nota VALUES (?, ?, ?)", (matricula, disciplina_id, valor))
    con.commit()
    con.close()


def listar_notas():
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        SELECT n.matricula, a.nome, n.disciplina_id, d.nome, n.valor
        FROM nota n
        JOIN aluno a ON n.matricula = a.matricula
        JOIN disciplina d ON n.disciplina_id = d.id
    """)
    dados = cur.fetchall()
    con.close()
    return dados


def atualizar_nota(matricula, disciplina_id, valor):
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        UPDATE nota
        SET valor=?
        WHERE matricula=? AND disciplina_id=?
    """, (valor, matricula, disciplina_id))
    con.commit()
    con.close()


def excluir_nota(matricula, disciplina_id):
    con = conectar()
    cur = con.cursor()
    cur.execute(
        "DELETE FROM nota WHERE matricula=? AND disciplina_id=?",
        (matricula, disciplina_id)
    )
    con.commit()
    con.close()
