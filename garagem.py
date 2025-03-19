import sqlite3


def criar_tabela():
    try:
        conexao = sqlite3.connect("garagem.db")
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS carros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                modelo TEXT NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                potencia INTEGER NOT NULL
            );
        """)

        conexao.commit()
        print("Tabela criada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        conexao.close()

criar_tabela()


def adicionar_carro(modelo, cor, ano, potencia):
    try:
        conexao = sqlite3.connect("garagem.db")
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO carros (modelo, cor, ano, potencia)
            VALUES (?, ?, ?, ?)
        """,(modelo, ano, cor, potencia))

        conexao.commit()
        print(f"Carro {modelo} adicionado com sucesso!")

    except sqlite3.Error as e:
        print(f"Erro ao adicionar carro {e}")

    finally:
        conexao.close()


def listar_carros():
    try:
        conexao = sqlite3.connect("garagem.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM carros")
        carros = cursor.fetchall()

        if carros:
            for carro in carros:
                print(f"ID: {carro[0]} | Modelo: {carro[1]} | Ano: {carro[2]} | Cor: {carro[3]} | Potência: {carro[4]} CV")
        else:
            print("Nenhum carro encontrado")
    except sqlite3.Error as e:
        print(f"Erro ao listar carro {e}")
    finally:
        conexao.close()


def atualizar_carro(id_carro, modelo=None, ano=None, cor=None, potencia=None):
    try:
        conexao = sqlite3.connect("garagem.db")
        cursor = conexao.cursor()

        if modelo:
            cursor.execute("UPDATE carros SET modelo = ? WHERE id = ?", (modelo, id_carro))
        if ano:
            cursor.execute("UPDATE carros SET ano = ? WHERE id = ?", (ano, id_carro))
        if cor:
            cursor.execute("UPDATE carros SET cor = ? WHERE id = ?", (cor, id_carro))
        if potencia:
            cursor.execute("UPDATE carros SET potencia = ? WHERE id = ?", (potencia, id_carro))

        conexao.commit()
        print(f"Carro ID {id_carro} atualizado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar carro {e}")
    finally:
        conexao.close()


def remover_carro(id_carro):
    pass