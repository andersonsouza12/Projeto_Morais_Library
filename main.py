import biblioteca

livro = dict()
livros = list()
continuar = " "
voltarMenu = " "
lista = []

while continuar != "sair":
    voltarMenu = " "
    print("""
    1 - Adcionar livros
    2 - Atualizar quantidade de livros
    3 - Remover titulos do acervo"
    4 - Mostrar dados do livro
    5 - Buscar por exemplares[ano, titulo, autor, assunto]"
    6 - Importar dados 
    7 - Obter status de um livro 
    8 - Gerar relatórios 
    9 - Alugar livro
    10 - Adicionar categoria
    11 - Sair
    """)
    escolha = int(input("O que voce deseja? "))
    if escolha == 1:
        while voltarMenu != "menu":
            livro = biblioteca.cadastroDeLivros()
            livros.append(livro.copy())
            voltarMenu = str(input("Digite MENU para voltar ao menu ou ENTER para continuar ").lower())

    elif escolha == 2:
        nome = str(input("Qual nome do livro que você quer mudar a quantidade?: "))
        valor = int(input("Novo valor de quantidade do livro: "))
        biblioteca.atualizarQuantidade(nome, valor, livros)

    elif escolha == 3:
        print("Deseja remover titulos do acervo por:"
              "\n1 - Por Ano (obs:. Serao removido qualquer titulo de mesmo ano ou de anos anteriores ao desejado)"
              "\n2 - Por titulo")
        desejo2 = int(input("Qual você deseja fazer? "))
        if desejo2 == 1:
            biblioteca.removerTitulos(desejo2, livros)
        if desejo2 == 2:
            biblioteca.removerTitulos(desejo2, livros)

    elif escolha == 4:
        nome = str(input("Qual nome do livro que você quer ver os dados?: "))
        for l in livros:
            if l["nome"] == nome:
                print(f"O nome do livro é {l['nome']}\n"
                      f"Ele é {l['fisicoOuEletronico']}\n"
                      f"Lançado em {l['anoLancamento']}")

    elif escolha == 5:  # buscar livros
        escolha = str(input('Como você quer buscar o livro? [ano, titulo, autor, assunto] ').lower())
        if escolha == 'ano':
            ano = int(input('Digite o ano para a pesquisa: '))
            for l in livros:
                if l['anoLancamento'] == ano:
                    lista.append(l['nome'])
            print(lista)
            lista.clear()
        elif escolha == 'titulo':
            titulo = input('Insira o titulo do livro: ').lower()
            for l in livros:
                if titulo in l['nome'].lower():
                    lista.append(l['nome'])
            print(lista)
            lista.clear()
        elif escolha == 'autor':
            autor = input('Insira o autor do livro: ').lower()
            for l in livros:
                if autor in l['autor'].lower():
                    lista.append(l['nome'])
            print(lista)
            lista.clear()
        elif escolha == 'assunto':
            assunto = input('Insira o assunto do livro: ').lower()
            for l in livros:
                if assunto in l['assunto'].lower():
                    lista.append(l['nome'])
            print(lista)
            lista.clear()

    elif escolha == 6:  # importar dados
        pass

    elif escolha == 7:  # obter status do livro
        titulo = str(input('Insira o titulo do livro para saber sua situação: ').lower())
        for l in livros:
            if l['nome'] == titulo:
                print(f"Situação do livro {l['nome']} é:\n"
                      f"A Quantidade disponível: {l['quantidade']}\n"
                      f"Esta alugado? :  {l['alugado']}\n"
                      f"Fim do Aluguel {l['dataAluguel']}")

    elif escolha == 8:
        print('1 - Gerar relatório do acervo \n2 - Gerar relatório por categoria \n' +
              '3 - Gerar relatório por assunto')
        escolha3 = int(input('O que você deseja? '))
        if escolha3 == 1:

            print('Gerando relatório...')
            relatorio = open('relatorioDoAcervo.txt', 'w', encoding="utf8")
            relatorio.writelines('RELATÓRIO DO ACERVO DA MORAIS LIBRARY \n\n')
            for l in livros:
                relatorio.writelines(f"Livro: {l['nome']} \n" +
                                     f"    Autor: {l['autor']}\n" +
                                     f"    Tipo: {l['fisicoOuEletronico']}\n" +
                                     f"    Ano da Edição: {l['anoLancamento']}\n" +
                                     f"    Assunto: {l['assunto']}\n" +
                                     f"    Quantidade: {l['quantidade']}\n" +
                                     f"    Alugado:  {l['alugado']}\n" +
                                     f"    Fim do Aluguel {l['dataAluguel']}"
                                     )
            relatorio.close()
            print('Relatório gerado com sucesso!!')

        elif escolha3 == 2:
            escolha4 = input('Digite a categoria a ser gerado o relatório: [A CATEGORIA -NAO FORNECIDO- É O PADRÃO'
                             ' CASO NÃO TENHAM CADASTRADO NENHUMA]').lower()
            print('Gerando relatório...')
            relatorio = open(f'Relatório - Categoria {escolha4}.txt', 'w', encoding="utf8")
            relatorio.write(f'RELATÓRIO SOBRE A CATEGORIA {escolha4.upper()}\n\n')
            for l in livros:
                if escolha4 == l['categoria']:
                    relatorio.write(f"    Livro: {l['nome']} \n" +
                                    f"    Autor: {l['autor']}\n" +
                                    f"    Tipo: {l['fisicoOuEletronico']}\n" +
                                    f"    Ano da Edição: {l['ano']}\n" +
                                    f"    Assunto: {l['assunto']}\n" +
                                    f"    Quantidade: {l['quantidade']}\n" +
                                    f"    Alugado:  {l['alugado']}\n" +
                                    f"    Fim do Aluguel {l['dataAluguel']}"
                                    )
            relatorio.close()
            print('Relatório gerado com sucesso!!')

        elif escolha3 == 3:
            escolha5 = input('Digite o assunto a ser gerado o relatório: ').lower()
            print('Gerando relatório...')
            relatorio = open(f'Relatório - Assunto {escolha5}.txt', 'w', encoding="utf8")
            relatorio.write(f'RELATÓRIO SOBRE O ASSUNTO {escolha5.upper()}\n\n')
            for l in livros:
                if escolha5 == l['assunto']:
                    relatorio.write(f"Livro: {l['nome']} \n" +
                                    f"    Autor: {l['autor']}\n" +
                                    f"    Tipo: {l['fisicoOuEletronico']}\n" +
                                    f"    Ano da Edição: {l['anoLancamento']}\n" +
                                    f"    Assunto: {l['assunto']}\n" +
                                    f"    Quantidade: {l['quantidade']}\n" +
                                    f"    Alugado:  {l['alugado']}\n" +
                                    f"    Fim do Aluguel {l['dataAluguel']}"
                                    )
            relatorio.close()
            print('Relatório gerado com sucesso!!')

    elif escolha == 9:
        biblioteca.alugarLivro(livros)

    # Alteração
    elif escolha == 10:
        biblioteca.adicionarcategoriaETematica(livros)
    # Fim da alteração

    elif escolha == 11:  # lembrar de corrigir aqui, e por sair como 11, la encima no primeiro print tbm
        continuar = 'sair'  # la vai estar como sair == 10
