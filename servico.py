import validacao

def menu_servicos(dados_servicos, grava_dados_servicos): 
    resp2 = ""
    while resp2 != '0':
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"|- \033[1;34m{'MÓDULO DE SERVIÇOS':^34}\033[m -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("|-  (1) - Cadastrar Novo Serviço      -|")
        print("|-  (2) - Pesquisar Serviço           -|")
        print("|-  (3) - Alterar Serviço             -|")
        print("|-  (4) - Excluir Serviço             -|")
        print("|-  (0) - Sair                        -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()
        resp2 = input("Escolha a opção desejada: ")
        print()
        
        if resp2 == '1':
            validacao.limpar()
            print('=' * 36)
            print(f" \033[1;35m {'CADASTRAR NOVO SERVIÇO':.^34} \033[m ")
            print('=' * 36)
            id_servico = validacao.criar_id(dados_servicos)
            print(f"|-- ID Gerado Automático: {id_servico}")
            nome_servico = input("|-- Nome do Serviço:   ")
            print('-' * 36)
            valor = input("|-- Valor (R$):        ")
            print('-' * 36)
            tempo = input("|-- Duração Estimada:  ").upper()
            print('=' * 36)
            print()
            dados_servicos[id_servico] = [nome_servico, valor, tempo, True]
            print("Serviços: ", dados_servicos)
            grava_dados_servicos(dados_servicos)
            print(f" \033[1;35m {'Serviço cadastrado ...'} \033[m ")
            alerta = (r"""
            >>=========================<<
            ||  NOVO SERVIÇO NA ÁREA!  ||
            ||  Cadastrado com êxito   ||
            >>=========================<<
            """)
            print(f"\033[1;33m {alerta} \033[m ")
            print()
            input("Tecle <ENTER> para continuar...")
            
        elif resp2 == '2':
            validacao.limpar()
            print('='*36)
            print(f" \033[1;35m {'PESQUISAR SERVIÇO':.^34} \033[m ")
            print('='*36)
            id_servico = input("Insira o ID do serviço, \npara pesquisar: ")
            print()
            
            # TRUQUE DE MESTRE: Busca tanto como texto quanto como número inteiro!
            if id_servico.isdigit() and int(id_servico) in dados_servicos:
                id_servico = int(id_servico)
                
            if id_servico in dados_servicos and len(dados_servicos[id_servico]) > 3 and dados_servicos[id_servico][-1] == True:
                print(" \033[1;35m Serviços cadastrados: \033[m ")
                print("|-- Nome do serviço: ", dados_servicos[id_servico][0], "--|")
                print("|-- Valor do serviço: ", dados_servicos[id_servico][1], "--|")
                print("|-- Duração estimada: ", dados_servicos[id_servico][2], "--|")
                print("=" * 36)
                print()
                print(f" \033[1;35m {'Pesquisa de serviços concluida...'} \033[m ")
                alerta = (r"""
                >>========================<<
                ||    BUSCA CONCLUÍDA! ツ  ||
                ||  Catálogo verificado... ||
                >>========================<<
                """)
                print(f"\033[1;33m {alerta} \033[m ")
            else:
                print()
                print(" \033[1;31m Serviço não encontrado no sistema! \033[m ")
                print()
            print()
            input("Tecle <ENTER> para continuar...")
            
        elif resp2 == '3':
            validacao.limpar()
            print('='*36)
            print(f" \033[1;35m {'ALTERAR SERVIÇO':.^34} \033[m ")
            print('='*36)
            id_servico = input("Insira o id do serviço, \npara alterar:  ")      
            print()
            
            # TRUQUE DE MESTRE: Busca tanto como texto quanto como número inteiro!
            if id_servico.isdigit() and int(id_servico) in dados_servicos:
                id_servico = int(id_servico)
                
            if id_servico in dados_servicos and len(dados_servicos[id_servico]) > 3 and dados_servicos[id_servico][-1] == True:
                print(" \033[1;35m Dados dos serviços cadastrados: \033[m ")
                print("|-- Nome do serviço: ", dados_servicos[id_servico][0], "--|")
                print("|-- Valor do serviço: ", dados_servicos[id_servico][1], "--|")
                print("|-- Duração estimada: ", dados_servicos[id_servico][2], "--|")
                print("=" * 36)
                print()
                print(" \033[1;35m Digite os novos dados: \033[m ")
                nome_servico = input("|-- Nome do Serviço:   ")
                print('-' * 36)
                valor = input("|-- Valor (R$):        ")
                print('-' * 36)
                tempo = input("|-- Duração Estimada:  ").upper()
                print('=' * 36)
                
                dados_servicos[id_servico] = [nome_servico, valor, tempo, True]
                grava_dados_servicos(dados_servicos)
                print()
                print(f" \033[1;35m {'alteração concluída...'} \033[m ")
                alerta = (r"""
            >>======================<<
            || Alteração Concluída  ||
            ||  Serviço atualizado  ||
            >>======================<<
            """)
                print(f"\033[1;33m {alerta} \033[m ")
            else:
                print(" \033[1;31m Serviço não encontrado no sistema! \033[m ")
            print() 
            input("Tecle <ENTER> para continuar...")   
            
        elif resp2 == '4':
            validacao.limpar()
            print('='*36)
            print(f" \033[1;35m {'EXCLUIR SERVIÇO':.^34} \033[m ")
            print('='*36)
            id_servico = input("Insira o ID do serviço, \npara excluir: ")
            print()
            
            # TRUQUE DE MESTRE: Busca tanto como texto quanto como número inteiro!
            if id_servico.isdigit() and int(id_servico) in dados_servicos:
                id_servico = int(id_servico)
                
            if id_servico in dados_servicos and len(dados_servicos[id_servico]) > 3 and dados_servicos[id_servico][-1] == True:
                print(" \033[1;35m Dados dos serviços cadastrados: \033[m ")
                print("|-- Nome do serviço: ", dados_servicos[id_servico][0], "--|")
                print("|-- Valor do serviço: ", dados_servicos[id_servico][1], "--|")
                print("|-- Duração estimada: ", dados_servicos[id_servico][2], "--|")
                print("=" * 36)
                print()
                verificar = input("Tecle 's' para confirmar exclusão...")
                if verificar.lower() == 's':
                    dados_servicos[id_servico][-1] = False
                    grava_dados_servicos(dados_servicos) 
                    print(f" \033[1;33m {'Exclusão do serviço concluída...'} \033[m ")
                    print()
                    print("Serviço:", dados_servicos)  
                    alerta = (r"""
            >>=====================<<
            ||   Serviço removido  ||
            >>=====================<<
            """)
                    print(f"\033[1;33m {alerta} \033[m ")
                else:
                    print(f" \033[1;35m {'exclusão cancelada ツ...'} \033[m ")
            else:
                print(f" \033[1;33m {'Serviço não encontrado ou já excluído!'} \033[m ")
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
            input("Tecle <ENTER> para continuar...")