from models.Bairro import Bairro
from utils.menus import sub_menu_consulta, sub_menu_atualizar, menu
from ..main import lista_bairros

def consultar_municipio():  # LISTA OS BAIRROS DO MUNICIPIO ESCOLHIDO
    while True:
        nome_municipio = input("\nQual município você procura? (Digite '0' para retornar): ").title()
        municipios_encontrados = [bairro for bairro in lista_bairros if nome_municipio == bairro.municipio.title()]
        if nome_municipio == '0':
            sub_menu_consulta()
        elif municipios_encontrados:
            print(f"\nBairros de {nome_municipio}:")
            for bairro in municipios_encontrados:
                print(f"\n- {bairro.bairro.upper()}\n Situação: {bairro.situacao}\n Nível Água: {bairro.nivel}m\n Alerta Evacuação: {bairro.alerta}\n Energia: {bairro.energia}\n Abastecimento de Água: {bairro.agua}")
            while True:
                    opcao = input("\nGostaria de saber informações de outro município? (s/n): ").lower()
                    if opcao == "s":
                        break
                    elif opcao == "n":
                        menu()
                    else:
                        print("OPÇÃO INVÁLIDA! Por favor, digite 's' para pesquisa ou 'n' para voltar ao menu inicial.")
        else:
            print("Nenhum município encontrado.")
            
def consultar_bairro_qry():  # LISTA AS INFORMAÇÕES DOS BAIRROS ENCONTRADOS (quando a função é chamada pelo sub_menu_consulta)
    while True:
        nome_bairro = input("\nQual bairro você procura? (Digite '0' para retornar): ").title()
        bairros_encontrados = [bairro for bairro in lista_bairros if nome_bairro == bairro.bairro.title()]
        if nome_bairro == '0':
            sub_menu_consulta()
        elif bairros_encontrados:
            count = len(bairros_encontrados)
            if count > 1:
                print(f"\n * {count} bairros encontrados: *")
            else:
                pass
            for bairro in bairros_encontrados:
                print(f"\n- {bairro.municipio.upper()}\n Bairro: {bairro.bairro}\n UF: {bairro.estado}\n Situação: {bairro.situacao}\n Nível Água: {bairro.nivel}m\n Alerta Evacuação: {bairro.alerta}\n Energia: {bairro.energia}\n Abastecimento de Água: {bairro.agua}")
            while True:
                    opcao = input("\nGostaria de saber informações de outro bairro? (s/n): ").lower()
                    if opcao == "s":
                        break
                    elif opcao == "n":
                        menu()
                    else:
                        print("OPÇÃO INVÁLIDA! Por favor, digite 's' para pesquisa ou 'n' para voltar ao menu inicial.")
        else:
            print("Nenhum bairro encontrado.")

def consultar_bairro_att():  # LISTA AS INFORMAÇÕES DOS BAIRROS ENCONTRADOS (quando a função é chamada pelo sub_menu_atualizar)
    while True:
        nome_bairro = input("\nQual bairro você procura? (Digite '0' para retornar): ").title()
        bairros_encontrados = [bairro for bairro in lista_bairros if nome_bairro == bairro.bairro.title()]
        if nome_bairro == '0':
            sub_menu_atualizar()
        elif bairros_encontrados:
            count = len(bairros_encontrados)
            if count > 1:
                print(f"\n * {count} bairros encontrados: *")
            else:
                pass
            for bairro in bairros_encontrados:
                print(f"\n- {bairro.municipio.upper()}\n Bairro: {bairro.bairro}\n UF: {bairro.estado}\n Situação: {bairro.situacao}\n Nível Água: {bairro.nivel}m\n Alerta Evacuação: {bairro.alerta}\n Energia: {bairro.energia}\n Abastecimento de Água: {bairro.agua}")
            while True:
                    opcao = input("\nGostaria de saber informações de outro bairro? (s/n): ").lower()
                    if opcao == "s":
                        break
                    elif opcao == "n":
                        sub_menu_atualizar()
                    else:
                        print("OPÇÃO INVÁLIDA! Por favor, digite 's' para pesquisa ou 'n' para voltar ao menu inicial.")
        else:
            print("Nenhum bairro encontrado.")