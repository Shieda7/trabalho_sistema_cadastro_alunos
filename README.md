# trabalho_sistema_cadastro_alunos

## 📌 Sobre o Projeto

Este projeto é um **Sistema de Cadastro de Alunos**, desenvolvido em Python com:

* **Tkinter** (interface gráfica)
* **SQLite** (banco de dados local)
* Arquitetura separada em módulos
* Suporte a exportação de dados em **CSV, JSON e TXT**

O sistema permite gerenciar:

* **Alunos**
* **Disciplinas**
* **Notas dos alunos**
* **Exportação de dados**

---

# 🗃️ Banco de Dados (SQLite)

O sistema utiliza SQLite por ser leve, rápido e não exigir servidor externo.

### 🔌 `conexao.py`

Arquivo responsável por:

* Criar a conexão com o banco (`sqlite3.connect()`)
* Criar as tabelas, caso não existam

As tabelas são:

### 📍 Tabela **aluno**

| Campo      | Tipo    | Descrição                     |
| ---------- | ------- | ----------------------------- |
| matricula  | TEXT PK | Identificador único do aluno  |
| nome       | TEXT    | Nome completo                 |
| nascimento | TEXT    | Data de nascimento YYYY-MM-DD |

### 📍 Tabela **disciplina**

| Campo     | Tipo    | Descrição             |
| --------- | ------- | --------------------- |
| id        | INTEGER | PK autoincrement      |
| nome      | TEXT    | Nome da disciplina    |
| turno     | TEXT    | Manhã / Tarde / Noite |
| sala      | TEXT    | Local da aula         |
| professor | TEXT    | Docente responsável   |

### 📍 Tabela **nota**

| Campo         | Tipo    | Descrição            |
| ------------- | ------- | -------------------- |
| matricula     | TEXT    | FK → aluno.matricula |
| disciplina_id | INTEGER | FK → disciplina.id   |
| valor         | REAL    | Nota numérica        |

---

# 🧩 Módulos do Banco de Dados

Cada arquivo em `database/` representa um CRUD.

---

## 📘 `aluno_db.py`

Contém funções como:

* `inserir_aluno()`
* `atualizar_aluno()`
* `excluir_aluno()`
* `listar_alunos()`

Exemplo de inserção:

```python
cur.execute("INSERT INTO aluno VALUES (?, ?, ?)", (matricula, nome, dt_nascimento))
```

---

## 📗 `disciplina_db.py`

Permite:

* Criar disciplina
* Alterar disciplina
* Excluir disciplina
* Listar disciplinas

---

## 📙 `nota_db.py`

Contém:

* CRUD de notas
* Listagem geral das notas com JOIN
* Listagem específica por aluno

Exemplo — listagem completa de notas:

```sql
SELECT n.matricula, a.nome, n.disciplina_id, d.nome, n.valor
FROM nota n
JOIN aluno a ON n.matricula = a.matricula
JOIN disciplina d ON n.disciplina_id = d.id
```

Exemplo — notas por aluno:

```sql
SELECT a.nome, d.nome, n.valor
FROM nota n
JOIN aluno a ON n.matricula = a.matricula
JOIN disciplina d ON n.disciplina_id = d.id
WHERE n.matricula = ?
```

---

# 🖥️ Interface Gráfica — `gui_main.py`

A interface é totalmente feita com **Tkinter + ttk**.

## 🎛️ Estrutura da GUI

A interface usa um **Notebook**, criando abas:

* **Alunos**
* **Disciplinas**
* **Notas**
* **Exportar Dados**

Cada aba possui:

* Formulário de entrada
* Tabela `Treeview` para visualização
* Botões de incluir, alterar, excluir
* Atualização automática ao salvar dados

---

## 🟦 Aba Alunos

Funcionalidades:

* Cadastrar aluno
* Alterar dados do aluno
* Excluir aluno
* Listar todos automaticamente

Componentes utilizados:

* `LabelFrame` para formulário
* `Entry` para inputs
* `Treeview` para tabela
* Botões conectados às funções de aluno_db

---

## 🟥 Aba Disciplinas

Possibilidades:

* Criar disciplina
* Alterar disciplina já existente
* Excluir disciplina
* Selecionar uma disciplina clicando na tabela (evento `TreeviewSelect`)

---

## 🟩 Aba Notas

Recursos:

* Registrar notas de alunos
* Alterar notas
* Excluir notas
* Mostrar tabela com JOIN entre aluno e disciplina

---

## 🟨 Aba Exportar Dados

Permite exportar:

* Tabela de alunos
* Tabela de disciplinas
* Tabela de notas
* Em formatos:

  * `.csv`
  * `.json`
  * `.txt`

A aba oferece:

* Combobox de tabelas
* Combobox de formatos
* Botão **Exportar**

---

# 📤 Exportação — `exportacao.py`

Arquivo responsável por gerar arquivos externos.

### ⚙ Como funciona?

A função:

```python
exportar(dados, nome_arquivo, formato)
```

Recebe:

* lista com os dados do banco
* nome do arquivo final
* formato

Suporta:

### 📑 CSV

Escreve linhas com `csv.writer`.

### 📑 JSON

Usa `json.dump()` com indentação.

### 📑 TXT

Salva cada linha formatada com `" | "` entre os valores.

Os arquivos sempre vão para a pasta:

```
dados/
```

---

# 🚀 Arquivo Principal — `main.py`

É o ponto de entrada do programa.

Executa:

1. `criar_tabelas()` → garante que o banco existe
2. `iniciar_gui()` → abre a interface gráfica

---

# 📦 Como Executar

### 1. Instale o Python 3.10+

### 2. Clone o repositório

### 3. Execute

# 🎯 Objetivo do Projeto

Este sistema foi desenvolvido com fins educacionais:

* praticar CRUD
* praticar Banco de Dados
* praticar Tkinter
* praticar organização modular de código
