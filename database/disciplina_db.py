from conexao import conectar

# -----------------------------------------------
# CRUD DISCIPLINA
# -----------------------------------------------
def inserir_disciplina(nome, turno, sala, professor):
    con = conectar()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO disciplina (nome, turno, sala, professor) VALUES (?, ?, ?, ?)",
        (nome, turno, sala, professor)
    )
    con.commit()
    con.close()


def listar_disciplinas():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM disciplina")
    dados = cur.fetchall()
    con.close()
    return dados


def atualizar_disciplina(id_disc, nome, turno, sala, professor):
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        UPDATE disciplina
        SET nome=?, turno=?, sala=?, professor=?
        WHERE id=?
    """, (nome, turno, sala, professor, id_disc))
    con.commit()
    con.close()


def excluir_disciplina(id_disc):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM disciplina WHERE id=?", (id_disc,))
    con.commit()
    con.close()
