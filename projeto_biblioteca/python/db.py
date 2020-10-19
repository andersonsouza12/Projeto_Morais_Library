import sqlite3

banco = sqlite3.connect("livros.db")

cursor = banco.cursor()

# Cria o Banco de dados
'''
cursor.execute("CREATE TABLE livros (id interger PRIMARY KEY, nome text, alugavel text, categoria text, tematica text, "
               "reserva text, quantidade interger, anoLancamento interger, fisicoOuEletronico text, alugado text)")
banco.commit()
'''
