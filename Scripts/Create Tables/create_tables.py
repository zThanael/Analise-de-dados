import sqlite3
import os

# os.remove('pesquisa_satisfacao.db') if os.path.exists('pesquisa_satisfacao.db') else None
conn = sqlite3.connect('pesquisa_satisfacao.db')

cur = conn.cursor()


sql_create_perguntas =  'CREATE TABLE IF NOT EXISTS perguntas'\
                        '(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'\
                        'enunciado VARCHAR(200) NOT NULL)';

sql_create_respostas =  'CREATE TABLE IF NOT EXISTS respostas'\
                        '(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'\
                        'resposta VARCHAR(30) NOT NULL,'\
                        'id_pergunta INTEGER NOT NULL,'\
                        'FOREIGN KEY (id_pergunta) REFERENCES perguntas(id))';

sql_creates = [sql_create_perguntas,sql_create_respostas]

exe_create = [cur.execute(sql_create) for sql_create in sql_creates]
print('Banco criado com sucesso')