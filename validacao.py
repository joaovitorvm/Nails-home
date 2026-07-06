import subprocess

def valida_telefone(numero):
    if len(numero) == 11 and numero.isdigit():
        return True   
    else:
        return False  

def valida_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    else:
        return True

def validar_email(email):
    if "@gmail.com" in email:
        return True
    else:
        return False

def limpar():
    subprocess.run("clear")
        
def criar_id(lista):
    from random import randint
    n5 = -1 
    while (n5 == -1) or (n5 in lista):         
        n1 = str(randint(0,9))
        n2 = str(randint(0,9))
        n3 = str(randint(0,9))
        n4 = str(randint(0,9))
        n5 = int(n1 + n2 + n3 + n4)
        c = 1
    return n5

def valida_aniversario(aniversario):
    if "/" in aniversario:
        print("Data de aniversario armazenada!")
        return True
    else:
        return False

def exibir_menu_principal():
    mensagem = (r"""
 _   _         _  _               _
| \ | |       (_)| |             | |
|  \| |  __ _  _ | | ___  ______ | |__    ___   _ __ ___    ___
| . ` | / _` || || |/ __||______|| '_ \  / _ \ | '_ ` _ \  / _ \
| |\  || (_| || || |\__ \        | | | || (_) || | | | | ||  __/
|_| \_| \__,_||_||_||___/        |_| |_| \___| |_| |_| |_| \___|
""")
    print(f" \033[1;35m {mensagem} \033[m ")
    print(f" \033[1;35m {'BOAS-VINDAS AO NAILS HOME  ^_^'} \033[m ")
    print()
    print(fr"{'=/'*17}\\")
    print(fr"|{'MÓDULO DE REGISTROS':.^34}|")
    print(fr"/|!/{'_'*30}\|")
    print(fr"/|{'_(1)-MÓDULO CLIENTES: _':.^32}\|")
    print(fr"/|{'_(2)-MÓDULO SERVIÇOS: _':.^32}\|")
    print(fr"/|{'_(3)-MÓDULO AGENDAMENTO: _':.^32}\|")
    print(fr"/|{'_(4)-MÓDULO RELATÓRIO: _':.^32}\|")
    print(fr"/|{'_(5)-MÓDULO SOBRE: _':.^32}\|")
    print(fr"/|{'_(0)-SAIR: _':.^32}\|")
    print(fr"/|!/{'_'*30}\!")
    print(fr"{'=/'*17}\\")
    print()