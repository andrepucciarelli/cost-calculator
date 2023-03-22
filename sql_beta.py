import pandas as pd
import sqlite3

# Criando o Conn
conn =  sqlite3.connect('sistema.db')
c = conn.cursor()

#Criar a tabela de dados para o cadastro do Material
c.execute("""CREATE TABLE IF NOT EXISTS materiais (
        Codigo text,
        Tipo text,
        Descricao text,
        Unidade text,
        Preco number)
        """)

# Ler as Tabelas e criar o DataFrame
df_material = pd.read_sql('SELECT * FROM materiais', conn)

# Fechar Conexão
conn.commit()
conn.close()