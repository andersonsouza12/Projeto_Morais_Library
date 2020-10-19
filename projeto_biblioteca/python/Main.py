import os
import Biblioteca


def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print("BEM VINDO AO SISTEMA DA MORAIS LIBRARY ")
    print("OQUE VOCE DESEJA? ")
    print("1 - CADASTRAR NOVOS LIVROS")
    print("2 - ATUALIZAR A QUANTIDADE DE ALGUM LIVRO?")
    print("3 - REMOVER TITULOS ANTIGOS")
    print("4 - BUSCAR POR TITULOS ELETRONICOS OU FISICOS")
    print("5 - OBTER STATUS DO LIVRO")
    print("6 - GERAR RELATORIOS")
    menuInput = int(input("DIGITE O NUMERO EQUIVALENTE E APERTE ENTER "))
    limparTela()
    return menuInput


def escolhas(desejo):
    if desejo == 1:
        Biblioteca.cadastroDeLivros()
        limparTela()
    elif desejo == 2:
        Biblioteca.atualizarQuantidadeDeUmTituloEspecifico()
        voltar = str(input("DESEJA VOLTAR AO MENU? [SIM / NAO]").lower())
        if voltar == "sim":
            limparTela()
            menu()
    elif desejo == 3:
        Biblioteca.removerTitulosDesatualizados()
        voltar = str(input("DESEJA VOLTAR AO MENU? [SIM / NAO]").lower())
        if voltar == "sim":
            limparTela()
            menu()
    elif desejo == 4:
        print("1 - TITULOS ELETRONICOS")
        print("2 - TITULOS FISICOS")
        print("3 - VOLTAR AO MENU")
        buscarEleFisi = int(input("QUE TIPO VOCÊ DESEJA BUSCAR? "))
        while 1 > buscarEleFisi > 3:
            buscarEleFisi = int(input("VALOR INVALIDO DIGITE NOVAMENTE\nQUE TIPO VOCÊ DESEJA BUSCAR? "))
        if buscarEleFisi == 1:
            Biblioteca.buscarExemplaresEletronicos()
            voltar = str(input("DESEJA VOLTAR AO MENU? [SIM / NAO]").lower())
            if voltar == "sim":
                limparTela()
                menu()
        elif buscarEleFisi == 2:
            Biblioteca.buscarExemplaresFisicos()
            voltar = str(input("DESEJA VOLTAR AO MENU? [SIM / NAO]").lower())
            if voltar == "sim":
                limparTela()
                menu()
        elif buscarEleFisi == 3:
            limparTela()
            menu()
    elif desejo == 5:
        Biblioteca.statusDoLivro()
        voltar = str(input("DESEJA VOLTAR AO MENU? [SIM / NAO]").lower())
        if voltar == "sim":
            limparTela()
            menu()
    elif desejo == 6:
        print("1 - RELATORIO SOBRE O ACERVO")
        print("2 - RELATORIO POR CATEGORIA DOS LIVROS")
        print("3 - RELATORIO POR TEMATICA DOS LIVROS")
        print("4 - VOLTAR AO MENU")
        tipoRelatorio = int(input("ESCOLHA: "))
        while 1 > tipoRelatorio > 4:
            tipoRelatorio = int(input("VALOR INVALIDO\nESCOLHA ENTRE 1 E 3: "))
        if tipoRelatorio == 1:
            Biblioteca.gerarRelatorioDoAcervo()
            voltar = str(input("DESEJA VOLTAR AO MENU? [SIM / NAO]").lower())
            if voltar == "sim":
                menu()
        elif tipoRelatorio == 2:
            Biblioteca.gerarRelatorioPorCategoriaLivro()
            voltar = str(input("DESEJA VOLTAR AO MENU? [SIM / NAO]").lower())
            if voltar == "sim":
                menu()
        elif tipoRelatorio == 3:
            Biblioteca.gerarRelatorioPorTematicaLivro()
            voltar = str(input("DESEJA VOLTAR AO MENU? [SIM / NAO]").lower())
            if voltar == "sim":
                menu()
        elif tipoRelatorio == 4:
            menu()


desejo = menu()
escolhas(desejo)
