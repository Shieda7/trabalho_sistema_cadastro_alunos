import sqlite3

DB_NAME = "alunos.db"

def conectar():
    return sqlite3.connect(DB_NAME)


def criar_tabelas():
    con = conectar()
    cur = con.cursor()

    # Tabela Aluno
    cur.execute("""
    CREATE TABLE IF NOT EXISTS aluno (
        matricula TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        dt_nascimento TEXT NOT NULL
    );
    """)

    # Tabela Disciplina
    cur.execute("""
    CREATE TABLE IF NOT EXISTS disciplina (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        turno TEXT NOT NULL,
        sala TEXT NOT NULL,
        professor TEXT NOT NULL
    );
    """)

    # Tabela Nota
    cur.execute("""
    CREATE TABLE IF NOT EXISTS nota (
        matricula TEXT NOT NULL,
        disciplina_id INTEGER NOT NULL,
        valor REAL NOT NULL,
        PRIMARY KEY (matricula, disciplina_id),
        FOREIGN KEY (matricula) REFERENCES aluno(matricula),
        FOREIGN KEY (disciplina_id) REFERENCES disciplina(id)
    );
    """)

    con.commit()
    con.close()
