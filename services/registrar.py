from models.Bairro import Bairro
from models.Municipio import Municipio
from utils.menus import sub_menu_registro, menu
from ..main import lista_bairros

def registrar_municipio():  # NOVO REGISTRO MUNICIPIO
    print("\nDIGITE OS DADOS DO MUNICIPIO")
    municipio = input("\n Nome do município ('0' para retornar): ").title()
    if municipio == "0":
        sub_menu_registro()
    else:
        pass
    estado = input(f" '{municipio}' pertence ao estado (UF): ").upper()
    print(f"\n UF: {estado}\n Município: {municipio}")
    while True:
        opcao = input("\nDeseja confirmar? (s/n): ").lower()
        if opcao == "s":
            novo_municipio = Municipio(estado, municipio)
            print(f" * MUNICÍPIO REGISTRADO COM SUCESSO! * ")
            while True:
                opcao = input("\nQuer fazer um novo registro? (s/n): ")
                if opcao == "s":
                    sub_menu_registro()
                elif opcao == "n":
                    menu()
                else:
                    print("OPÇÃO INVÁLIDA! Por favor, digite 's' para novo registro ou 'n' para voltar ao Menu Inicial.")
        elif opcao == "n":
            registrar_municipio()
        else:
            print("OPÇÃO INVÁLIDA! Por favor, digite 's' para confirmar ou 'n' para editar.")

def registrar_bairro():  # NOVO REGISTRO BAIRRO
    print("\nDIGITE OS DADOS DO BAIRRO")
    bairro = input("\n Nome do bairro ('0' para retornar): ").title()
    if bairro == "0":
        sub_menu_registro()
    else:
        pass
    municipio = input(f" '{bairro}' pertence ao município: ").title()
    estado = input(f" '{municipio}' pertence ao estado (UF): ").upper()
    while True:
        print(f"\n UF: {estado}\n Município: {municipio}\n Bairro: {bairro}")
        opcao = input("\nDeseja confirmar? (s/n): ").lower()
        if opcao == "s":
            while True:
                print("\nDIGITE AS INFORMAÇÕES DO BAIRRO ('0' CANCELA)")
                situacao = input("\n Situação (Inacessível | Parcialmente Acessível | Acessível): ").title()
                if situacao == "0":
                    sub_menu_registro()
                nivel = float(input(" Nível Água (metros): "))
                alerta = input(" Alerta Evacuação (Seguro | Moderado | Crítico | Urgente): ").title()
                energia = input(" Energia (Sim | Não): ").title()
                agua = input(" Abastecimento Água (Sim | Não): ").title()
                while True:
                    print(f"\n- {bairro.upper()}\n Município: {municipio}\n Estado: {estado}\n Situação: {situacao}\n Nível Água: {nivel}m\n Alerta Evacuação: {alerta}\n Energia: {energia}\n Abastecimento de Água: {agua}")
                    opcao = input("\nDeseja confirmar? (s/n): ").lower()
                    if opcao == "s":
                        novo_bairro = Bairro(estado, municipio, bairro, situacao, nivel, alerta, energia, agua)
                        lista_bairros.append(novo_bairro)
                        print(f" * BAIRRO REGISTRADO COM SUCESSO! * ")
                        while True:
                            opcao = input("\nQuer fazer um novo registro? (s/n): ").lower()
                            if opcao == "s":
                                sub_menu_registro()
                            elif opcao == "n":
                                menu()
                            else:
                                print("OPÇÃO INVÁLIDA! Por favor, digite 's' para novo registro ou 'n' para voltar ao Menu Inicial.")
                    elif opcao == "n":
                        break
                    else:
                        print("OPÇÃO INVÁLIDA! Por favor, digite 's' para confirmar ou 'n' para editar.")
        elif opcao == "n":
            registrar_municipio()
        else:
            print("OPÇÃO INVÁLIDA! Por favor, digite 's' para confirmar ou 'n' para editar.")