def menu_relatorios(dados_clientes, dados_servicos, dados_agendamentos):
    resp4 = ''
    while resp4 != '0':
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"|- \033[1;34m{'MÓDULO DE RELATÓRIOS':^34}\033[m -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("|-  (1) - Clientes Ativos             -|")
        print("|-  (2) - Aniversariantes do Mês      -|")
        print("|-  (3) - Serviços Cadastrados        -|")
        print("|-  (4) - Todos os Agendamentos       -|")
        print("|-  (5) - Agendamentos por Dia        -|")
        print("|-  (6) - Serviço Mais Procurado      -|")
        print("|-  (0) - Voltar                      -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()
        
        resp4 = input("Escolha a opção desejada: ")
        print()
        
        if resp4 == '1':
            print()
            print(fr"{'=/'*17}\\")
            print(fr"|{'RELATÓRIO: CLIENTES ATIVOS':.^34}|")
            print(fr"/|!/{'_'*30}\|")
            print()
            for cpf, lista in dados_clientes.items():
                if len(lista) > 5 and lista[5] == True:
                    print(f"""
|-- CPF: {cpf}
-------------------
|-- Nome: {lista[1]}
-------------------      
|-- Telefone: {lista[0]}
-------------------
|-- E-mail: {lista[2]}
-------------------
|-- Aniversário: {lista[3]}""")
            print()
            input("Tecle <ENTER> para continuar...")
            
        elif resp4 == '2':
            print()
            print(fr"{'=/'*17}\\")
            print(fr"|{'RELATÓRIO: CLIENTES ANIVERSARIANTES':.^34}|")
            print(fr"/|!/{'_'*30}\|")
            print()
            mes_buscado = input("Digite o mês desejado (Ex: 01, 02...): ")
            for cpf, lista in dados_clientes.items():
                if len(lista) > 5 and lista[5] == True:
                    aniversario = str(lista[3]).split("/")
                    if len(aniversario) > 1 and mes_buscado == aniversario[1]:
                        print(f"""
    |-- Cliente Aniversariante!--|
    |-- Nome: {lista[1]}--|
    |-- Data de Nascimento: {lista[3]}--|
    |-- Número: {lista[0]}--|""")
            print()
            input("Tecle <ENTER> para continuar...")
            
        elif resp4 == '3':
            print()
            print(fr"{'=/'*17}\\")
            print(fr"|{'RELATÓRIO: SERVIÇOS CADASTRADOS':.^34}|")
            print(fr"/|!/{'_'*30}\|")
            print()
            for id_servico, lista in dados_servicos.items():
                if len(lista) > 3 and lista[3] == True:
                    print(f"""
    |-- ID Cadastrado: {id_servico}
    |-- Nome do serviço: {lista[0]}
    |-- Valor do serviço: R$ {lista[1]}
    |-- Duração estimada: {lista[2]}""")
            print()
            input("Tecle <ENTER> para continuar...")
            
        elif resp4 == '4':
            print()
            print(fr"{'=/'*17}\\")
            print(fr"|{'RELATÓRIO: TODOS AGENDAMENTOS':.^34}|")
            print(fr"/|!/{'_'*30}\|")
            print()
            for id_agendamento, lista in dados_agendamentos.items():
                if len(lista) > 4 and lista[4] == True:
                    print(f"""
    |-- ID Cadastrado: {id_agendamento}
    |-- Cliente: {lista[0]}
    |-- Serviço: {lista[1]}
    |-- Dia:     {lista[2]}
    |-- Horário: {lista[3]}""")
            print()
            input("Tecle <ENTER> para continuar...")
                
        elif resp4 == '5':
            print()
            print(fr"{'=/'*17}\\")
            print(fr"|{'RELATÓRIO: AGENDAMENTOS DO DIA':.^34}|")
            print(fr"/|!/{'_'*30}\|")
            print()
            dia_buscado = input("Digite o dia desejado (Ex: SEG, SAB...): ").upper()
            for id_agendamento, lista in dados_agendamentos.items():
                if len(lista) > 4 and lista[4] == True:
                    if dia_buscado == lista[2]:
                        print(f"""
    |-- ID do Agendamento: {id_agendamento}
    |-- Cliente: {lista[0]}
    |-- Serviço: {lista[1]}
    |-- Horário Marcado: {lista[3]}""")
            print()
            input("Tecle <ENTER> para continuar...")
            
        elif resp4 == '6':
            print()
            print(fr"{'=/'*17}\\")
            print(fr"|{'RELATÓRIO: SERVIÇOS MAIS PROCURADOS':.^34}|")
            print(fr"/|!/{'_'*30}\|")
            print()
            maior_procura = 0 
            servico_campeao = ""
            for id_servico, lista_servico in dados_servicos.items():
                if len(lista_servico) > 3 and lista_servico[3] == True:
                    contagem = 0
                    for id_agendamento, lista_agenda in dados_agendamentos.items():
                        if len(lista_agenda) > 4 and lista_agenda[4] == True:
                            if lista_agenda[1] == lista_servico[0]:
                                contagem = contagem + 1
                    if contagem > maior_procura:
                        maior_procura = contagem
                        servico_campeao = lista_servico[0]
            print()
            print(f" \033[1;33m >> O Serviço mais procurado: {servico_campeao} << \033[m ")
            print(f" \033[1;33m >> Total de Agendamentos: {maior_procura} << \033[m ")
            print("=" * 36)
            print()
            input("Tecle <ENTER> para continuar...")
            
        elif resp4 == '0':
            print("Voltando ao menu principal...")
            print()
        else:
            print(" \033[1;31m Opção inválida! \033[m ")
            print()
            input("Tecle <ENTER> para continuar...")
            print()
