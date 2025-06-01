menu = """

    Selecione uma opção:

    0 -> Crédito
    1 -> Débito
    2 -> Relatório
    3 -> Finalizar

    -> """

caixa = 0
limite_valor = 500
relatorio = ""
qtd_debitos = 0
LIMITE_DEBITOS = 3

def credito():
    valor_credito = float(input("Informe o valor para crédito: "))
    if valor_credito > 0:
        return valor_credito
    else:
        print("Valor inválido.")
        return 0

def mostrar_relatorio(caixa, relatorio):
    print("\n===== RELATÓRIO DE MOVIMENTAÇÃO =====")
    if relatorio == "":
        print("Não há registros até o momento.")
    else:
        print(relatorio)
    print(f"Saldo atual: R$ {caixa:.2f}")
    print("=====================================\n")

def debito(caixa, limite_valor, qtd_debitos, LIMITE_DEBITOS):
    if qtd_debitos >= LIMITE_DEBITOS:
        print("Limite de débitos diários atingido.")
        return caixa, qtd_debitos, ""

    valor_debito = float(input("Informe o valor para débito: "))

    if valor_debito <= 0:
        print("Erro: valor inválido.")
    elif valor_debito > limite_valor:
        print("Erro: valor excede o limite permitido.")
    elif valor_debito > caixa:
        print("Erro: saldo insuficiente.")
    else:
        caixa -= valor_debito
        qtd_debitos += 1
        print("Débito realizado com sucesso!")
        return caixa, qtd_debitos, f"Débito: -R$ {valor_debito:.2f}\n"

    return caixa, qtd_debitos, ""

while True:
    escolha = int(input(menu))

    if escolha == 0:
        valor_creditado = credito()
        if valor_creditado > 0:
            caixa += valor_creditado
            relatorio += f"Crédito: +R$ {valor_creditado:.2f}\n"
            print("Crédito efetuado!")

    elif escolha == 1:
        caixa, qtd_debitos, movimentacao = debito(caixa, limite_valor, qtd_debitos, LIMITE_DEBITOS)
        relatorio += movimentacao

    elif escolha == 2:
        mostrar_relatorio(caixa, relatorio)

    elif escolha == 3:
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")