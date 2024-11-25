from utils.menus import sub_menu_atualizar, menu
from ..main import lista_bairros

def atualizar_bairro():
    while True:
        nome_bairro = input("\nQual bairro você quer atualizar as informações? (Digite '0' para retornar): ").title()
        bairros_encontrados = [bairro for bairro in lista_bairros if nome_bairro == bairro.bairro.title()]
        if nome_bairro == '0':
            sub_menu_atualizar()
        elif bairros_encontrados:
            count = len(bairros_encontrados)
            if count > 1:
                print(f"\n * {count} bairros encontrados: *")
                count = 1
                for bairro in bairros_encontrados:
                    print(f"\n({count}) - {bairro.municipio.upper()}\n Bairro: {bairro.bairro}\n UF: {bairro.estado}\n Situação: {bairro.situacao}\n Nível Água: {bairro.nivel}m\n Alerta Evacuação: {bairro.alerta}\n Energia: {bairro.energia}\n Abastecimento de Água: {bairro.agua}")
                    count += 1
                while True:
                    opcao = input("\nQual bairro você quer atualizar? ('0' para retornar): ")
                    if opcao.isdigit():
                        opcao = int(opcao)
                        escolha = bairros_encontrados[opcao - 1]
                        nova_situacao = input(f"\n Qual a situação atual do bairro {escolha.bairro}? (Situação: {escolha.situacao}): ")
                        novo_nivel = float(input(f" Qual o nível atual da água no bairro {escolha.bairro}? (Nível da água: {escolha.nivel}m): "))
                        novo_alerta = input(f" Qual o alerta atual do bairro {escolha.bairro}? (Alerta: {escolha.alerta}): ")
                        nova_energia = input(f" Tem energia no bairro {escolha.bairro}? (Energia: {escolha.energia}): ")
                        nova_agua = input(f" Tem abastecimento de água no bairro {escolha.bairro}? (Abastecimento de água: {escolha.agua}): ")
                        while True:
                            print("\n * INFORMAÇÕES ATUALIZADAS *")
                            print(f"\n- {escolha.bairro.upper()}\n Município: {escolha.municipio}\n UF: {escolha.estado}\n Situação: {nova_situacao}\n Nível Água: {novo_nivel}m\n Alerta Evacuação: {novo_alerta}\n Energia: {nova_energia}\n Abastecimento de Água: {nova_agua}")
                            opcao = input("\nDeseja confirmar? (s/n): ").lower()
                            if opcao == "s":
                                bairro.situacao = nova_situacao
                                bairro.nivel = novo_nivel
                                bairro.alerta = novo_alerta
                                bairro.energia = nova_energia
                                bairro.agua = nova_agua
                                print(f"\n * BAIRRO ATUALIZADO COM SUCESSO! *")
                                while True:
                                    opcao = input("\nQuer fazer uma nova atualização? (s/n): ").lower()
                                    if opcao == "s":
                                        atualizar_bairro()
                                    elif opcao == "n":
                                        menu()
                                    else:
                                        print("OPÇÃO INVÁLIDA! Por favor, digite 's' para novo registro ou 'n' para voltar ao Menu Inicial.")
                            elif opcao == "n":
                                break
                            else:
                                print("OPÇÃO INVÁLIDA! Por favor, digite 's' para confirmar ou 'n' para editar.")
                    else:
                        print("\nOPÇÃO INVÁLIDA! Por favor, digite um número.")
            else:
                for bairro in bairros_encontrados:
                    print(f"\n- {bairro.bairro.upper()}\n Município: {bairro.municipio}\n UF: {bairro.estado}\n Situação: {bairro.situacao}\n Nível Água: {bairro.nivel}m\n Alerta Evacuação: {bairro.alerta}\n Energia: {bairro.energia}\n Abastecimento de Água: {bairro.agua}")
                while True:
                    print(f"\n Atualize as informações do bairro {bairro.bairro} ('0' para retornar)")
                    nova_situacao = input(f"\n Qual a situação atual do bairro {bairro.bairro}? (Situação: {bairro.situacao}): ")
                    if nova_situacao == '0':
                        sub_menu_atualizar()
                    else:
                        pass
                    novo_nivel = float(input(f" Qual o nível atual da água no bairro {bairro.bairro}? (Nível da água: {bairro.nivel}m): "))
                    novo_alerta = input(f" Qual o alerta atual do bairro {bairro.bairro}? (Alerta: {bairro.alerta}): ")
                    nova_energia = input(f" Tem energia no bairro {bairro.bairro}? (Energia: {bairro.energia}): ")
                    nova_agua = input(f" Tem abastecimento de água no bairro {bairro.bairro}? (Abastecimento de água: {bairro.agua}): ")
                    while True:
                        print("\n * INFORMAÇÕES ATUALIZADAS *")
                        print(f"\n- {bairro.bairro.upper()}\n Município: {bairro.municipio}\n UF: {bairro.estado}\n Situação: {nova_situacao}\n Nível Água: {novo_nivel}m\n Alerta Evacuação: {novo_alerta}\n Energia: {nova_energia}\n Abastecimento de Água: {nova_agua}")
                        opcao = input("\nDeseja confirmar? (s/n): ").lower()
                        if opcao == "s":
                            bairro.situacao = nova_situacao
                            bairro.nivel = novo_nivel
                            bairro.alerta = novo_alerta
                            bairro.energia = nova_energia
                            bairro.agua = nova_agua
                            print(f"\n * BAIRRO ATUALIZADO COM SUCESSO! * ")
                            while True:
                                opcao = input("\nQuer fazer uma nova atualização? (s/n): ")
                                if opcao == "s":
                                    atualizar_bairro()
                                elif opcao == "n":
                                    menu()
                                else:
                                    print("OPÇÃO INVÁLIDA! Por favor, digite 's' para novo registro ou 'n' para voltar ao Menu Inicial.")
                        elif opcao == "n":
                            break
                        else:
                            print("OPÇÃO INVÁLIDA! Por favor, digite 's' para confirmar ou 'n' para editar.")
        else:
            print("Nenhum bairro encontrado.")