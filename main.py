import pickle
import validacao
import clientes
import servico
import agendamento
import subprocess


def recupera_dados_clientes():
    try:
        dados_clientes={}
        arqDados = open("dadosClientes.dat", "rb")
        dados_clientes = pickle.load(arqDados)
        arqDados.close()
    except:
        dados_clientes = { 
            '71100736450': ["João Vitor","joaovitorvenanciomedeiros@gmail.com","19/02/2008","S",True]
        }
        arqDados = open("dadosClientes.dat", "wb")
        pickle.dump(dados_clientes, arqDados)
        arqDados.close()
    return dados_clientes
dados_clientes = recupera_dados_clientes()
dados_servicos = {'1234' : ["Mão", "25.00", "1 hora"]}
try:
    arqServic = open("dadosService.dat", "rb")
    dados_servicos = pickle.load(arqServic)
    arqServic.close()
except:
    arqServic = open("dadosService.dat", "wb")
    pickle.dump(dados_servicos, arqServic) 
    arqServic.close()

dados_agendamentos = {'123' : ["84999000466","1234","09/06","16:45"]}
try:
    arqAgendamento = open("dadosAgendamento.dat", "rb")
    dados_agendamentos = pickle.load(arqAgendamento)
    arqAgendamento.close()
except:
    arqAgendamento = open("dadosAgendamento.dat", "wb")
    pickle.dump(dados_agendamentos, arqAgendamento) 
    arqAgendamento.close()

def grava_dados_clientes(dados_clientes):
    arqDados = open("dadosClientes.dat", "wb")
    pickle.dump(dados_clientes, arqDados)
    arqDados.close()

def grava_dados_servicos(dados_servicos):
    arqServic = open("dadosService.dat", "wb")
    pickle.dump(dados_servicos, arqServic)
    arqServic.close()

def grava_dados_agendamentos(dados_agendamentos): 
    arqAgendamento = open("dadosAgendamento.dat", "wb")
    pickle.dump(dados_agendamentos, arqAgendamento)
    arqAgendamento.close()


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
        clientes.menu_clientes(dados_clientes, grava_dados_clientes)
    elif resp == '2':
        servico.menu_servicos(dados_servicos, grava_dados_servicos)
    elif resp == '3':
        agendamento.menu_agendamentos(dados_agendamentos, grava_dados_agendamentos)
    elif resp == '4':
        validacao.limpar()
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
        validacao.limpar()
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
        validacao.limpar()
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

grava_dados_clientes(dados_clientes)
grava_dados_servicos(dados_servicos)
grava_dados_agendamentos(dados_agendamentos)

    
