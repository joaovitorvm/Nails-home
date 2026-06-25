import os

dados_clientes = { '84999000466': ["João Vitor","S"]
}

dados_servicos = {'1234' : ["Mão", "25.00", "1 hora"]
}
dados_agendamentos = {'123' : ["84999000466","1234","09/06","16:45"]
}

resp = '10'

while (resp != '0'): 
    os.system('cls || clear')
    mensagem = (r"""
 _   _         _  _               _
| \ | |       (_)| |             | |
|  \| |  __ _  _ | | ___  ______ | |__    ___   _ __ ___    ___
| . ` | / _` || || |/ __||______|| '_ \  / _ \ | '_ ` _ \  / _ \
| |\  || (_| || || |\__ \        | | | || (_) || | | | | ||  __/
|_| \_| \__,_||_||_||___/        |_| |_| \___/ |_| |_| |_| \___|
""")

    print(f" \033[1;35m {mensagem} \033[m ")

    print(f" \033[1;35m {"BOAS-VINDAS AO NAILS HOME  ^_^"} \033[m ")
    print()

    print(fr"{'=/'*17}\\")
    print(fr"|{'MODÚLO DE REGISTROS':.^34}|")
    print(fr"/|!/{'_'*30}\|")
    print(fr"/|{'_(1)-MODÚLO CLIENTES: _':.^32}\|")
    print(fr"/|{'_(2)-MODÚLO SERVIÇOS: _':.^32}\|")
    print(fr"/|{'_(3)-MODÚLO AGENDAMENTO: _':.^32}\|")
    print(fr"/|{'_(4)-MODÚLO RELATÓRIO: _':.^32}\|")
    print(fr"/|{'_(5)-MODÚLO SOBRE: _':.^32}\|")
    print(fr"/|{'_(0)-SAIR: _':.^32}\|")
    print(fr"/|!/{'_'*30}\!")
    print(fr"{'=/'*17}\\")
    print()
    resp = input("Selecione uma das opções: ")
    print()
    
    if resp == '1':
        os.system('cls || clear')
        print(fr"{'=/'*17}\\")
        print(fr"|{'MODÚLO CLIENTES':.^34}|")
        print(fr"/|!/{'_'*30}\|")
        print(fr"/|{'_(1)-CADASTRAR: _':.^32}\|")
        print(fr"/|{'_(2)-ATUALIZAR: _':.^32}\|")
        print(fr"/|{'_(3)-PESQUISAR: _':.^32}\|")
        print(fr"/|{'_(4)-EXCLUIR: _':.^32}\|")
        print(fr"/|{'_(0)-SAIR: _':.^32}\|")
        print(fr"/|!/{'_'*30}\!")
        print(fr"{'=/'*17}\\")
        print()
        resp1 = input("Selecione uma das opções: ")
        print()
        
        if resp1 == '1':
            os.system('cls || clear')
            print('='*36)
            print(f" \033[1;35m {'CADASTRAR CLIENTES':.^34} \033[m ")
            print('='*36)
            nome = input("|-- Nome: ")
            print("-" * 30)
            numero = input("|-- Número: ( ) ")
            print("-" * 30)
            contato = input("|-- Primeira vez: [S/N] ").upper()
            print("=" * 36)
            print()
            dados_clientes[numero] = [nome,contato]
            print("Cliente: ",dados_clientes)
            print(f" \033[1;35m {'Realizando cadastro...'} \033[m ")
            alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
            print(f"\033[1;33m {alerta} \033[m ")
            print()
            input("Tecle <ENTER> para continuar...")
        elif resp1 == '2':
           os.system('cls || clear')
           print('='*36)
           print(f" \033[1;35m {'ATUALIZAR CLIENTE':.^34} \033[m ")
           print('='*36)
           numero = input("Insira o numero do cliente,\npara atualizar o seu cadastro: ")
           print()
           if numero in dados_clientes:     
               print("|-- Dados atuais da cliente: ")  
               print("|-- Nome: ",dados_clientes[numero][0])
               print("|-- Primeira vez: ",dados_clientes[numero][1])
               print("=" * 36)
               print()
               print(" \033[1;35m Digite os novos dados: \033[m ")
               nome = input("|-- Nome: ")
               print("-" * 30)
               contato = input("|-- Primeira vez: [S/N] ").upper()
               print("=" * 36)
               dados_clientes[numero] = [nome,contato]
           else:
              print(" \033[1;31m Cliente não encontrada no sistema! \033[m ")
              print()
           alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()      
           input("Tecle <ENTER> para continuar...")   
        elif resp1 == '3':
           os.system('cls || clear')
           print('='*36)
           print(f" \033[1;35m {'PESQUISAR CLIENTE':.^34} \033[m ")
           print('='*36)
           numero = input("Insira o número do cliente, \npara pesquisar: ")
           print()
           if numero in dados_clientes:
               print(" \033[1;35m Dados cadastrados: \033[m ")
               print("|-- Nome: ",dados_clientes[numero][0],"--|")
               print("|-- Primeira vez: ",dados_clientes[numero][1],"--|")
               print()
           else:
              print()
              print(" \033[1;31m Cliente não encontrado no sistema! \033[m ")
              print()
           print(f" \033[1;35m {'Pesquisa concluida...'} \033[m ")
           alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()  
           input("Tecle <ENTER> para continuar...")
           
        elif resp1 == '4':
           os.system('cls || clear')
           print('='*36)
           print(f" \033[1;35m {'EXCLUIR CLIENTE':.^34} \033[m ")
           print('='*36)
           numero = input("Insira o numero do cliente, \npara excluir: ")
           if numero in dados_clientes:
              print("|-- Dados atuais da cliente: ")  
              print("|-- Nome: ",dados_clientes[numero][0])
              print("|-- Primeira vez: ",dados_clientes[numero][1])
              verificar = input("Tecle 's' para confirmar exclusão...")
              if verificar.lower() == 's':
                  del dados_clientes[numero]
                  print(f" \033[1;33m {'Exclusão do cliente concluída...'} \033[m ")
                  print()
                  print("Cliente:",dados_clientes)
              else:
                  print(f" \033[1;35m {'exclusão cancelada ツ...'} \033[m ")
           else:
                  print(f" \033[1;33m {'Cliente não encontrado!'} \033[m ")
                  print()        
           print()
           alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()  
           input("Tecle <ENTER> para continuar...")
        elif resp1 == '0':
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
        

    elif resp == '2':
        print(fr"{'=/'*17}\\")
        print(fr"|{'MODÚLO SERVIÇOS':.^34}|")
        print(fr"/|!/{'_'*30}\|")
        print(fr"/|{'_(1)-CADASTRAR NOVO SERVIÇO _':.^32}\|")
        print(fr"/|{'_(2)-PESQUISAR SERVIÇO _':.^32}\|")
        print(fr"/|{'_(3)-ALTERAR _':.^32}\|")
        print(fr"/|{'_(4)-EXCLUIR _':.^32}\|")
        print(fr"/|{'_(0)-SAIR _':.^32}\|")
        print(fr"/|!/{'_'*30}\!")
        print(fr"{'=/'*17}\\")
        print()
        resp2 = input("Selecione uma das opções: ")
        print()
        if resp2 == '1':
           os.system('cls || clear')
           print('=' * 36)
           print(f" \033[1;35m {'CADASTRAR NOVO SERVIÇO':.^34} \033[m ")
           print('=' * 36)
           id_servico = input("|-- Código/ID do Serviço:   ")
           print('=' * 36) 
           servico = input("|-- Nome do Serviço:   ")
           print('-' * 36)
           valor = input("|-- Valor (R$):        ")
           print('-' * 36)
           tempo = input("|-- Duração Estimada:  ").upper()
           print('=' * 36)
           print()
           dados_servicos[id_servico] = [servico, valor, tempo]
           print("Serviços: ",dados_servicos)
           print(f" \033[1;35m {'Serviço cadastrado ...'} \033[m ")
           alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()
           input("Tecle <ENTER> para continuar...")
        elif resp2 == '2':
           os.system('cls || clear')
           print('='*36)
           print(f" \033[1;35m {'PESQUISAR SERVIÇO':.^34} \033[m ")
           print('='*36)
           id_servico = input("Insira o ID do serviço, \npara pesquisar: ")
           print()
           if id_servico in dados_servicos:
               print(" \033[1;35m Serviços cadastrados: \033[m ")
               print("|-- Nome do serviço: ",dados_servicos[id_servico][0],"--|")
               print("|-- Valor do serviço: ",dados_servicos[id_servico][1],"--|")
               print("|-- Duração estimada: ",dados_servicos[id_servico][2],"--|")
               print("=" * 36)
               print()
           else:
              print()
              print(" \033[1;31m Serviços não encontrado no sistema! \033[m ")
              print()
           print(f" \033[1;35m {'Pesquisa de serviços concluida...'} \033[m ")
           alerta =(r"""
                >>=====================<<
                ||   ESTE MODULO AINDA ||
                ||   SENDO PREPARADO   ||
                ||                     ||
                >>=====================<<
                """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()
           input("Tecle <ENTER> para continuar...")
        elif resp2 == '3':
           os.system('cls || clear')
           print('='*36)
           print(f" \033[1;35m {'ALTERAR SERVIÇO':.^34} \033[m ")
           print('='*36)
           id_servico = input("Insira o id do serviço, \npara alterar:  ")      
           print()
           if id_servico in dados_servicos:
               print(" \033[1;35m Dados dos serviços cadastrados: \033[m ")
               print("|-- Nome do serviço: ",dados_servicos[id_servico][0],"--|")
               print("|-- Valor do serviço: ",dados_servicos[id_servico][1],"--|")
               print("|-- Duração estimada: ",dados_servicos[id_servico][2],"--|")
               print("=" * 36)
               print()
               print(" \033[1;35m Digite os novos dados: \033[m ")
               servico = input("|-- Nome do Serviço:   ")
               print('-' * 36)
               valor = input("|-- Valor (R$):        ")
               print('-' * 36)
               tempo = input("|-- Duração Estimada:  ").upper()
               print('=' * 36)
               dados_servicos[id_servico] = [servico,valor,tempo]
               print()
               print(f" \033[1;35m {'alteração concluída...'} \033[m ")

           else:
               print(" \033[1;31m Serviço não encontrado no sistema! \033[m ")
               print()
               alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
               print(f"\033[1;33m {alerta} \033[m ")
               print() 
               input("Tecle <ENTER> para continuar...")   
        elif resp2 == '4':
           os.system('cls || clear')
           print('='*36)
           print(f" \033[1;35m {'EXCLUIR SERVIÇO':.^34} \033[m ")
           print('='*36)
           id_servico = input("Insira o ID do serviço, \npara excluir: ")
           if id_servico in dados_servicos:
               print(" \033[1;35m Dados dos serviços cadastrados: \033[m ")
               print("|-- Nome do serviço: ",dados_servicos[id_servico][0],"--|")
               print("|-- Valor do serviço: ",dados_servicos[id_servico][1],"--|")
               print("|-- Duração estimada: ",dados_servicos[id_servico][2],"--|")
               print("=" * 36)
               print()
               verificar = input("Tecle 's' para confirmar exclusão...")
               if verificar.lower() == 's':
                  del dados_servicos[id_servico]
                  print(f" \033[1;33m {'Exclusão do serviço concluída...'} \033[m ")
                  print()
                  print("Serviço:",dados_servicos)  
               else:
                  print(f" \033[1;35m {'exclusão cancelada ツ...'} \033[m ")
           else:
              print(f" \033[1;33m {'Serviço não encontrado!'} \033[m ")
              print()  
           print()
           alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()
           input("Tecle <ENTER> para continuar...")
        elif resp2 == '0':
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
        
        

            
    elif resp == '3':
        os.system('cls || clear')
        print(fr"{'=/'*17}\\")
        print(fr"|{'MODÚLO AGENDAMENTO':.^34}|") 
        print(fr"/|!/{'_'*30}\|")
        print(fr"/|{'_(1)-AGENDAR NOVO HORÁRIO _':.^32}\|")
        print(fr"/|{'_(2)-VISUALIZAR AGENDA _':.^32}\|")
        print(fr"/|{'_(3)-ALTERAR HORÁRIO _':.^32}\|")
        print(fr"/|{'_(4)-CANCELAR _':.^32}\|")
        print(fr"/|{'_(0)-SAIR _':.^32}\|")
        print(fr"/|!/{'_'*30}\!")
        print(fr"{'=/'*17}\\")
        print()
        resp3 = input("Selecione uma das opções: ")
        print()
        if resp3 == '1':
            os.system('cls || clear')
            print('='*36)
            print(f" \033[1;35m {'AGENDAR NOVO HORÁRIO':.^34} \033[m ")
            print('='*36)
            id_agendamento = input("Código do agendamento: ")
            print()
            print(" \033[1;35m Digite os dados do agendamento: \033[m ")
            cliente = input("|-- Nome do Cliente:     ")
            print('-' * 36)
            servico = input("|-- Serviço desejado:    ")
            print('-' * 36)
            dia = input("|-- Dia (Ex: SEG/SAB):   ")
            print('-' * 36)
            horario = input("|-- Horário (ex: 14:30): ")
            print('=' * 36)
            print()
            dados_agendamentos[id_agendamento] = [cliente, servico, dia, horario]
            print()
            print(f" \033[1;35m {'Horário cadastrado com sucesso...'} \033[m ")
            alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
            print(f"\033[1;33m {alerta} \033[m ")
            print()
            input("Tecle <ENTER> para continuar...")
        elif resp3 == '2':
          os.system('cls || clear')
          print('='*36)
          print(f" \033[1;35m {'VISUALIZAR HORÁRIO':.^34} \033[m ")
          print('='*36)
          id_agendamento = input("Insira o Código do agendamento: ")
          print()
          if id_agendamento in dados_agendamentos:
            print(" \033[1;35m Dados da Marcação: \033[m ")
            print("|-- Cliente: ", dados_agendamentos[id_agendamento][0])
            print("|-- Serviço: ", dados_agendamentos[id_agendamento][1])
            print("|-- Dia:     ", dados_agendamentos[id_agendamento][2])
            print("|-- Horário: ", dados_agendamentos[id_agendamento][3])
            print("=" * 36)
            print()
          else:
            print(" \033[1;31m Agendamento não encontrado no sistema! \033[m ")
            print()
            print(f" \033[1;35m {'Pesquisa concluída...'} \033[m ")
          alerta =(r"""
          >>=====================<<
          ||   ESTE MODULO AINDA ||
          ||   SENDO PREPARADO   ||
          ||                     ||
          >>=====================<<
          """)
          print(f"\033[1;33m {alerta} \033[m ")
          print()
          input("Tecle <ENTER> para continuar...")
        elif resp3 == '3':
            os.system('cls || clear')
            print('='*36)
            print(f" \033[1;35m {'ALTERAR HORÁRIO':.^34} \033[m ")
            print('='*36)
            id_agendamento = input("Insira o Código do agendamento \npara alterar: ")
            print()
            if id_agendamento in dados_agendamentos:
               print(" \033[1;35m Dados da Marcação: \033[m ")             
               print("|-- Cliente: ", dados_agendamentos[id_agendamento][0])
               print("|-- Serviço: ", dados_agendamentos[id_agendamento][1])
               print("|-- Dia:     ", dados_agendamentos[id_agendamento][2])
               print("|-- Horário: ", dados_agendamentos[id_agendamento][3])
               print("=" * 36)
               print()
               print(" \033[1;35m Digite os novos dados: \033[m ")
               cliente = input("|-- Nome do Cliente:     ")
               print('-' * 36)
               servico = input("|-- Serviço desejado:    ")
               print('-' * 36)
               dia = input("|-- Dia (Ex: SEG/SAB):   ")
               print('-' * 36)
               horario = input("|-- Horário (ex: 14:30): ")
               print('=' * 36)
               dados_agendamentos[id_agendamento] = [cliente, servico, dia, horario]
               print()
               print(f" \033[1;35m {'Alteração concluída...'} \033[m ")
            else:
                print(" \033[1;31m Agendamento não encontrado no sistema! \033[m ")
                print()
                alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
            print(f"\033[1;33m {alerta} \033[m ")
            print()
            input("Tecle <ENTER> para continuar...")
        elif resp3 == '4':
            os.system('cls || clear')
            print('='*36)
            print(f" \033[1;35m {'CANCELAR HORÁRIO':.^34} \033[m ")
            print('='*36)
            id_agendamento = input("Insira o Código do agendamento \npara cancelar: ")
            print()
            if id_agendamento in dados_agendamentos:
               print(" \033[1;35m Dados da Marcação: \033[m ")             
               print("|-- Cliente: ", dados_agendamentos[id_agendamento][0])
               print("|-- Serviço: ", dados_agendamentos[id_agendamento][1])
               print("|-- Dia:     ", dados_agendamentos[id_agendamento][2])
               print("|-- Horário: ", dados_agendamentos[id_agendamento][3])
               print("=" * 36)
               print()
               verificar = input("Tecle 's' para confirmar exclusão...")
               if verificar.lower() == 's':
                  del dados_agendamentos[id_agendamento]
                  print(f" \033[1;33m {'Exclusão do agendamento concluída...'} \033[m ")
                  print()
                  print("Agendamento:",dados_agendamentos)  
               else:
                  print(f" \033[1;35m {'exclusão cancelada ツ...'} \033[m ")
            else:
                print(f" \033[1;33m {'Agendamento não encontrado!'} \033[m ")
                print()  
                print()  
            alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
            print(f"\033[1;33m {alerta} \033[m ")
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
        

    elif resp == '4':
        os.system('cls || clear')
        print('='*36)
        print(fr"|{'MODÚLO RELATÓRIO':.^34}|")
        print(fr"/|!/{'_'*30}\|")
        print(fr"/|{'_(1)-FATURAMENTO TOTAL: _':.^32}\|")
        print(fr"/|{'_(2)-MEIOS DE PAGAMENTO: _':.^32}\|")
        print(fr"/|{'_(3)-CONTROLE DE DESPESAS: _':.^32}\|")
        print(fr"/|{'_(0)-SAIR: _':.^32}\|")
        print(fr"/|!/{'_'*30}\!")
        print(fr"{'=/'*17}\\")
        print()
        resp4 = input("Selecione uma das opções: ")
        print()    
        if resp4 == '1':
           print('='*36)
           print(f" \033[1;35m {'FATURAMENTO TOTAL':.^34} \033[m ")
           print('='*36) 
    elif resp == '5':
        os.system('cls || clear')
        saida = (r"""
        >>======================<<
        || <<< MÓDULO SOBRE >>> ||
        **************************
        ||     OBRIGADO POR     ||
        ||UTILIZAR O GERENCIADOR||
        ||     NAILS HOUSE :)   ||
        >>======================<<
        """)
        print(f" \033[1;35m {saida} \033[m ")

    elif resp== '0':
        os.system('cls || clear')
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

    #fim da primeira parte
    
    