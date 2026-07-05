import subprocess
def valida_telefone(numero):
    if len(numero) == 11 and numero.isdigit():
        return True   
    else:
        return False  
def valida_cpf(cpf):
    if  len(cpf) != 11  or not cpf.isdigit():
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

    
#def valida_cpf
#validar data
