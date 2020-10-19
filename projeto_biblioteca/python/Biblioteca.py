import db


def cadastroDeLivros():
    continuar = " "
    while continuar != "N":
        id = int(input("DIGITE A ID DO LIVRO EM VALORES NUMERICOS\nQUAL A ID DO LIVRO? "))
        nome = str(input("QUAL O NOME DO LIVRO? "))
        alugavel = str(input("ESTE LIVRO É ALUGAVEL? [SIM / NÃO]").lower())
        while alugavel != "sim" and alugavel != "nao":
            alugavel = str(input("VALOR INVALIDO, DIGITE SIM OU NÃO\nESTE LIVRO É ALUGAVEL? ").lower())

        reservavel = str(input("ESTE LIVRO PODE SER RESERVADO? "))
        while reservavel != "sim" and alugavel != "não":
            reservavel = str(input("VALOR INVALIDO, DIGITE SIM OU NÃO\nESTE LIVRO PODE SER RESERVADO? "))

        quantidade = int(input("QUANTOS EXEMPLARES VAI CADASTRAR? "))
        anoLancamento = int(input("QUAL O ANO DE LANÇAMENTO? "))
        fisicoOuEletronico = str(input("LIVRO FISICO OU ELETRONICO? "))
        while fisicoOuEletronico != "fisico" and fisicoOuEletronico != "eletronico":
            fisicoOuEletronico = str(input("DIGITE APENAS SE É FISICO OU ELETRONICO: "))
        db.cursor.execute("INSERT INTO livros VALUES('" + str(id) + "', '" + nome + "', '" + alugavel + "', 'SEM DADOS', 'SEM DADOS', '" + reservavel + "', '" + str(
            quantidade) + "', '" + str(anoLancamento) + "', '" + fisicoOuEletronico + "', 'NAO')")
        db.banco.commit()
        continuar = str(input("VOCE DESEJA CONTINUAR CADASTRANDO? [S / N]").upper())


def cadastrarCategoriaETematicas():
    id = int(input("QUAL A ID DO LIVRO QUE VOCÊ DESEJA CADASTRAR A CATEGORIA? "))
    categoria = str(input("QUAL A CATEGORIA DESTE LIVRO?"))
    db.cursor.execute("UPDATE livros SET categoria = '" + categoria + "' WHERE id ='" + str(id) + "' ")
    db.banco.commit()
    tematica = str(input("E QUAL A TEMATICA DESTE LIVRO?"))
    db.cursor.execute("UPDATE livros SET categoria = '" + tematica + "' WHERE id ='" + str(id) + "' ")
    db.banco.commit()
    print("CATEGORIA E TEMATICA ATUALIZADAS")


def atualizarQuantidadeDeUmTituloEspecifico():
    id = int(input("QUAL O ID DO LIVRO QUE VOCE DESEJA MUDAR A QUANTIDADE? "))
    novoValor = int(input("NOVA QUANTIDADE DE TITULOS DISPONIVEIS: "))
    db.cursor.execute("UPDATE livros SET quantidade = '" + str(novoValor) + "' WHERE id ='" + str(id) + "' ")
    print("VALOR ATUALIZADO")
    db.banco.commit()


def removerTitulosDesatualizados():
    removerDesatualizado = int(input("REMOVER TITULOS DE QUE ANO? "))
    db.cursor.execute("DELETE FROM livros WHERE anoLancamento = '" + str(removerDesatualizado) + "' ")
    db.banco.commit()
    print("TITULOS REMOVIDOS")


def buscarExemplaresFisicos():
    db.cursor.execute("SELECT nome FROM livros WHERE fisicoOuEletronico = 'fisico' ")
    print("OS LIVROS FISICOS QUE POSSUIMOS SÃO: ")
    for c in db.cursor.fetchall():
        print(c)


def buscarExemplaresEletronicos():
    db.cursor.execute("SELECT nome FROM livros WHERE fisicoOuEletronico = 'eletronico' ")
    print("OS LIVROS EM FORMATO ELETRONICO QUE POSSUIMOS SÃO: ")
    for c in db.cursor.fetchall():
        print(c)


def alugarLivro():
    alugar = str(input("DESEJA ALUGAR UM LIVRO? [SIM / NÃO]").lower())
    while alugar != "sim" and alugar != "nao":
        alugar = str(input("DESEJA ALUGAR UM LIVRO? APERNAS SIM / NÃO ").lower())
    if alugar == "sim":
        id = int(input("ID DO LIVRO PARA O ALUGUEL "))
        db.cursor.execute("SELECT alugavel FROM livros WHERE id = '" + str(id) + "' ")
        for linha in db.cursor.fetchall():
            if linha[0] == "sim":
                db.cursor.execute("UPDATE livros SET alugado = '" + str(alugar) + "' WHERE id ='" + str(id) + "' ")
                db.banco.commit()
            elif linha[0] == "nao":
                print("O LIVRO NÃO PODE SER ALUGADO")


def statusDoLivro():
    status = str(input("ID DO LIVRO PARA VERIFICAÇÃO: "))
    db.cursor.execute("SELECT alugado FROM livros WHERE id = '" + status + "' ")
    for linha in db.cursor.fetchall():
        if linha[0] == 's':
            print("ESTE LIVRO ESTA ALUGADO")
        elif linha[0] == "n":
            print("ESTE LIVRO NÃO ESTA ALUGADO")


def gerarRelatorioDoAcervo():
    db.cursor.execute("SELECT nome FROM livros")
    arquivo = open("relatorio.txt", "w")
    arquivo.write("RELATORIO DO ACERVO DA BIBLIOTECA\n\n")

    for tabela in db.cursor.fetchall():
        arquivo.writelines(f"Nome do livro: {tabela}\n")
    print("RELATORIO CONCLUIDO COM SUCESSO")


def gerarRelatorioPorCategoriaLivro():
    categoria = str(input("QUAL CATEGORIA VOCÊ DESEJA VER OS TITULOS? "))
    db.cursor.execute("SELECT nome FROM livros WHERE categoria = '" + categoria + "' ")
    arquivo = open("relatorioPorCategoria", "w")
    arquivo.write(f"RELATORIO DO ACERVO DA BIBLIOTECA PELA CATEGORIA: {categoria.upper()} \n\n")

    for tabela in db.cursor.fetchall():
        arquivo.writelines(f"Nome do livro: {tabela}\n")

    print("RELATORIO CONCLUIDO COM SUCESSO")


def gerarRelatorioPorTematicaLivro():
    tematica = str(input("QUAL A TEMATICA DOS LIVROS QUE VOCÊ DESEJA VER? ").lower())
    db.cursor.execute("SELECT nome FROM livros WHERE tematica = '" + tematica + "' ")
    arquivo = open("relatorioPorTematica", "w")
    arquivo.write(f"RELATORIO DO ACERVO DA BIBLIOTECA PELA TEMATICA: {tematica.upper()} \n\n")

    for tabela in db.cursor.fetchall():
        arquivo.writelines(f"Nome do livro: {tabela}\n")

    print("RELATORIO CONCLUIDO COM SUCESSO")

