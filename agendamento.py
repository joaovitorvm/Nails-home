import validacao

def menu_agendamentos(dados_agendamentos, grava_dados_agendamentos):
    resp3 = ""
    while resp3 != '0': 
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"|- \033[1;34m{'MÓDULO DE AGENDAMENTO':^34}\033[m -|") 
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("|-  (1) - Agendar Novo Horário        -|")
        print("|-  (2) - Visualizar Agenda           -|")
        print("|-  (3) - Alterar Horário             -|")
        print("|-  (4) - Cancelar Horário            -|")
        print("|-  (0) - Sair                        -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()
        resp3 = input("Escolha a opção desejada: ")
        print()
        
        if resp3 == '1':
            validacao.limpar()
            print('='*36)
            print(f" \033[1;35m {'AGENDAR NOVO HORÁRIO':.^34} \033[m ")
            print('='*36)
            id_agendamento = validacao.criar_id(dados_agendamentos)
            print(f"|-- Código Gerado Automático: {id_agendamento}")
            print()
            print(" \033[1;35m Digite os dados do agendamento: \033[m ")
            cliente = input("|-- Nome do Cliente:     ")
            print('-' * 36)
            nome_servico = input("|-- Serviço desejado:    ") 
            print('-' * 36)
            dia = input("|-- Dia (Ex: SEG/SAB):     ")
            print('-' * 36)
            horario = input("|-- Horário (ex: 14:30): ")
            print('=' * 36)
            print()
            
            dados_agendamentos[id_agendamento] = [cliente, nome_servico, dia, horario, True]
            grava_dados_agendamentos(dados_agendamentos)
            
            print(f" \033[1;35m {'Horário cadastrado com sucesso...'} \033[m ")
            alerta = (r"""
            >>=========================<<
            ||    HORÁRIO RESERVADO!   ||
            ||  Agendamento concluído  ||
            >>=========================<<
            """)
            print(f"\033[1;33m {alerta} \033[m ")
            print()
            input("Tecle <ENTER> para continuar...")
            
        elif resp3 == '2':
            validacao.limpar()
            print('='*36)
            print(f" \033[1;35m {'VISUALIZAR HORÁRIO':.^34} \033[m ")
            print('='*36)
            id_agendamento = input("Insira o Código do agendamento: ")
            print()       
            if id_agendamento in dados_agendamentos and len(dados_agendamentos[id_agendamento]) > 4 and dados_agendamentos[id_agendamento][-1] == True:
                print(" \033[1;35m Ficha da Marcação: \033[m ")
                print(f"|-- Cliente: {dados_agendamentos[id_agendamento][0]}")
                print(f"|-- Serviço: {dados_agendamentos[id_agendamento][1]}")
                print(f"|-- Dia:     {dados_agendamentos[id_agendamento][2]}")
                print(f"|-- Horário: {dados_agendamentos[id_agendamento][3]}")
                print("=" * 36)
                print()
                print(f" \033[1;35m {'Pesquisa concluída...'} \033[m ")
                alerta = (r"""
            >>=========================<<
            ||     BUSCA CONCLUÍDA!    ||
            ||    Agenda verificada    ||
            >>=========================<<
            """)
                print(f"\033[1;33m {alerta} \033[m ")
            else:
                print(" \033[1;31m Agendamento não encontrado ou cancelado! \033[m ")
            print()
            input("Tecle <ENTER> para continuar...")
            
        elif resp3 == '3':
            validacao.limpar()
            print('='*36)
            print(f" \033[1;35m {'ALTERAR HORÁRIO':.^34} \033[m ")
            print('='*36)
            id_agendamento = input("Insira o Código do agendamento para alterar: ")
            print()
            if id_agendamento in dados_agendamentos and len(dados_agendamentos[id_agendamento]) > 4 and dados_agendamentos[id_agendamento][-1] == True:
                print(" \033[1;35m Dados Atuais da Marcação: \033[m ")             
                print(f"|-- Cliente: {dados_agendamentos[id_agendamento][0]}")
                print(f"|-- Serviço: {dados_agendamentos[id_agendamento][1]}")
                print(f"|-- Dia:     {dados_agendamentos[id_agendamento][2]}")
                print(f"|-- Horário: {dados_agendamentos[id_agendamento][3]}")
                print("=" * 36)
                print()
                print(" \033[1;35m Digite os novos dados: \033[m ")
                cliente = input("|-- Nome do Cliente:     ")
                print('-' * 36)
                nome_servico = input("|-- Serviço desejado:    ") 
                print('-' * 36)
                dia = input("|-- Dia (Ex: SEG/SAB):     ")
                print('-' * 36)
                horario = input("|-- Horário (ex: 14:30): ")
                print('=' * 36)
                
                dados_agendamentos[id_agendamento] = [cliente, nome_servico, dia, horario, True]
                grava_dados_agendamentos(dados_agendamentos)
                
                print()
                print(f" \033[1;35m {'Alteração concluída...'} \033[m ")
                alerta = (r"""
                >>=========================<<
                ||  AGENDAMENTO RENOVADO!  ||
                ||    Horário atualizado   ||
                >>=========================<<
                """)
                print(f"\033[1;33m {alerta} \033[m ")
            else:
                print(" \033[1;31m Agendamento não encontrado no sistema! \033[m ")
            print()
            input("Tecle <ENTER> para continuar...")
            
        elif resp3 == '4':
            validacao.limpar()
            print('='*36)
            print(f" \033[1;35m {'CANCELAR HORÁRIO':.^34} \033[m ")
            print('='*36)
            id_agendamento = input("Insira o Código do agendamento para cancelar: ")
            print()
            
            if id_agendamento in dados_agendamentos and len(dados_agendamentos[id_agendamento]) > 4 and dados_agendamentos[id_agendamento][-1] == True:
                print(" \033[1;35m Dados da Marcação: \033[m ")             
                print(f"|-- Cliente: {dados_agendamentos[id_agendamento][0]}")
                print(f"|-- Serviço: {dados_agendamentos[id_agendamento][1]}")
                print(f"|-- Dia:     {dados_agendamentos[id_agendamento][2]}")
                print(f"|-- Horário: {dados_agendamentos[id_agendamento][3]}")
                print("=" * 36)
                print()
                
                verificar = input("Tecle 's' para confirmar o cancelamento: ")
                if verificar.lower() == 's':
                    dados_agendamentos[id_agendamento][-1] = False
                    grava_dados_agendamentos(dados_agendamentos)
                    
                    print()
                    print(f" \033[1;33m {'Cancelamento concluído com sucesso...'} \033[m ")
                    alerta = (r"""
                    >>=========================<<
                    ||    HORÁRIO CANCELADO    ||
                    ||    Horário liberado!    ||
                    >>=========================<<
                    """)
                    print(f"\033[1;33m {alerta} \033[m ")
                else:
                    print()
                    print(f" \033[1;35m {'Operação cancelada ツ...'} \033[m ")
            else:
                print(f" \033[1;33m {'Agendamento não encontrado ou já cancelado!'} \033[m ")
            print()
            input("Tecle <ENTER> para continuar...")
            
        elif resp3 == '0':
            saida = (r"""
            >>======================<<
            || <<< MÓDULO SAÍDA >>> ||
            **************************
            ||     OBRIGADO POR     ||
            ||UTILIZAR O GERENCIADOR||
            ||     NAILS HOUSE :)   ||
            >>======================<<
            """)     
            print(f" \033[1;35m {saida} \033[m ")
            input("Tecle <ENTER> para continuar...")
