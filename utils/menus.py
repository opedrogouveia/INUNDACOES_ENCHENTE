from services.consultar import consultar_municipio, consultar_bairro_qry, consultar_bairro_att
from services.registrar import registrar_municipio, registrar_bairro
from services.atualizar import atualizar_bairro

def menu():  # MENU INICIAL
    while True:
        try:
            opcao = int(input("\n  * REGIÕES AFETADAS *  \n 1 - Consultar região.\n 2 - Novo Registro.\n 3 - Atualizar região.\n 0 - Encerrar.\nDigite um número: "))
            if opcao == 1:
                sub_menu_consulta()
            elif opcao == 2:
                sub_menu_registro()
            elif opcao == 3:
                sub_menu_atualizar()
            elif opcao == 0:
                while True:
                    opcao = input("Deseja encerrar o sistema? (s/n) ").lower()
                    if opcao == "s":
                        print("Encerrando...")
                        exit()
                    elif opcao == "n":
                        print("Continuando...")
                        break
                    else:
                        print("\nOPÇÃO INVÁLIDA! Por favor, digite 's' para encerrar ou 'n' para continuar.")
            else:
                    print("\nOPÇÃO INVÁLIDA! Por favor, escolha uma das opções abaixo.")
        except ValueError:
            print("\nOPÇÃO INVÁLIDA! Por favor, digite um número.")

def sub_menu_consulta():  # SUB-MENU CONSULTAR POR MUNICIPIO/REGIÃO
    while True:
        opcao = input("\n 1 - Consultar por Municipio.\n 2 - Consultar por Bairro.\n 0 - Retornar\nDigite um número: ")
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 1:
                consultar_municipio()
            elif opcao == 2:
                consultar_bairro_qry()
            elif opcao == 0:
                menu()
        else:
            print("\nOPÇÃO INVÁLIDA! Por favor, digite um número.")

def sub_menu_registro():  # SUB-MENU REGISTRAR MUNICIPIO/BAIRRO
    while True:
        opcao = input("\n 1 - Registrar novo município.\n 2 - Registrar novo bairro.\n 0 - Retornar\nDigite um número: ")
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 1:
                registrar_municipio()
            elif opcao == 2:
                registrar_bairro()
            elif opcao == 0:
                menu()
        else:
            print("\nOPÇÃO INVÁLIDA! Por favor, digite um número.")

def sub_menu_atualizar():  # SUB-MENU ATUALIZAR DADOS BAIRRO
    while True:
        opcao = input("\n 1 - Atualizar bairro.\n 2 - Verificar situação atual dos bairros.\n 0 - Retornar\nDigite um número: ")
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 1:
                atualizar_bairro()
            elif opcao == 2:
                consultar_bairro_att()
            elif opcao == 0:
                menu()
        else:
            print("\nOPÇÃO INVÁLIDA! Por favor, digite um número.")