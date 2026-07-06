import relatorios

def listar_todos_clientes(dados_clientes):
    print()
    print(fr"{'=/'*17}\\")
    print(fr"|{'RELATÓRIO: CLIENTES ATIVOS':.^34}|")
    print(fr"/|!/{'_'*30}\|")
    print()

    for cpf, lista in dados_clientes.items():
        if lista[5] == True:
            print(f"""CPF: {cpf}
-------------------
Nome: {lista[1]}
-------------------      
Telefone: {lista[0]}
-------------------
E-mail: {lista[2]}
-------------------
Aniversário: {lista[3]}""")
            
def listar_clientes_aniversariantes(dados_clientes):
    print()
    print(fr"{'=/'*17}\\")
    print(fr"|{'RELATÓRIO: CLIENTES ANIVERSARIANTES':.^34}|")
    print(fr"/|!/{'_'*30}\|")
    print()
    mes_buscado = input("Digite o mês desejado (Ex: 01, 02...): ")
    for cpf, lista in dados_clientes.items():
        if lista[5] == True:
            aniversario = lista[3].split("/")
            if mes_buscado == aniversario[1]:
                print(f"""
    -- Cliente Aniversariante!
    -- Nome: {lista[1]}
    -- Data de Nascimento: {lista[3]}
    -- Número: {lista[0]}""")
# =========================================================
# MÓDULO DE RELATÓRIOS DO SISTEMA (MAPA DEFINITIVO)
# =========================================================

# 1. RELATÓRIO DE CLIENTES ATIVOS (Concluído ✔️)
# -> Lista todos os clientes cadastrados com status ativo.

# 2. RELATÓRIO DE CLIENTES ANIVERSARIANTES (Concluído ✔️)
# -> Filtra os clientes que fazem aniversário no mês buscado.

# 3. RELATÓRIO DE SERVIÇOS CADASTRADOS (Para amanhã ⏳)
# -> Lista todos os serviços, preços e durações oferecidos pelo salão.

# 4. RELATÓRIO DE TODOS OS AGENDAMENTOS (Para amanhã ⏳)
# -> Mostra o histórico geral da agenda do sistema.

# 5. RELATÓRIO DE AGENDAMENTOS DO DIA (Para amanhã ⏳)
# -> Filtra a agenda para mostrar apenas os clientes marcados para hoje.

# 6. RELATÓRIO DE SERVIÇOS MAIS PROCURADOS (Para amanhã ⏳)
# -> Analisa e exibe os serviços campeões de vendas/agendamentos.
