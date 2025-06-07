import datetime

clientes = []
contas_bancarias = []

MAX_SAQUES_DIARIOS = 3
VALOR_MAXIMO_SAQUE = 500.0

def cadastrar_cliente():
    cpf_cliente = input("Informe o CPF (apenas números): ")
    cliente = next((c for c in clientes if c["cpf"] == cpf_cliente), None)

    if cliente:
        print("Este cliente já está cadastrado.")
        return

    nome_completo = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco_completo = input("Endereço (logradouro, nº - bairro - cidade/UF): ")

    clientes.append({
        "nome": nome_completo,
        "data_nasc": nascimento,
        "cpf": cpf_cliente,
        "endereco": endereco_completo
    })
    print("✅ Cliente cadastrado com sucesso!")

def abrir_conta():
    cpf_cliente = input("Digite o CPF do cliente: ")
    cliente = next((c for c in clientes if c["cpf"] == cpf_cliente), None)

    if not cliente:
        print("Cliente não encontrado.")
        return

    numero_da_conta = len(contas_bancarias) + 1
    contas_bancarias.append({
        "agencia": "0001",
        "numero": numero_da_conta,
        "cliente": cliente,
        "saldo": 0.0,
        "saques_efetuados": 0,
        "movimentacoes": []
    })
    print(f"✅ Conta número {numero_da_conta} criada!")

def realizar_deposito(conta):
    try:
        valor_deposito = float(input("Informe o valor para depósito: "))
    except ValueError:
        print("❌ Valor inválido.")
        return

    if valor_deposito > 0:
        conta["saldo"] += valor_deposito
        conta["movimentacoes"].append(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}: Depósito de R$ {valor_deposito:.2f}")
        print("💰 Depósito efetuado com sucesso!")
    else:
        print("❌ Valor precisa ser positivo.")

def realizar_saque(conta):
    if conta["saques_efetuados"] >= MAX_SAQUES_DIARIOS:
        print("❌ Você atingiu o limite diário de saques.")
        return

    try:
        valor_saque = float(input("Informe o valor para saque: "))
    except ValueError:
        print("❌ Valor inválido.")
        return

    if valor_saque <= 0:
        print("❌ O valor deve ser maior que zero.")
    elif valor_saque > conta["saldo"]:
        print("❌ Saldo insuficiente.")
    elif valor_saque > VALOR_MAXIMO_SAQUE:
        print(f"❌ O limite máximo por saque é R$ {VALOR_MAXIMO_SAQUE:.2f}.")
    else:
        conta["saldo"] -= valor_saque
        conta["saques_efetuados"] += 1
        conta["movimentacoes"].append(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}: Saque de R$ {valor_saque:.2f}")
        print("💸 Saque realizado!")

def mostrar_extrato(conta):
    print("\n📜 Histórico de movimentações:")
    if not conta["movimentacoes"]:
        print(" - Nenhuma movimentação registrada.")
    else:
        for item in conta["movimentacoes"]:
            print(" -", item)
    print(f"\n💰 Saldo atual: R$ {conta['saldo']:.2f}")

def escolher_conta():
    if not contas_bancarias:
        print("⚠️ Ainda não há contas cadastradas.")
        return None

    for c in contas_bancarias:
        print(f"{c['numero']}: {c['cliente']['nome']} (CPF: {c['cliente']['cpf']})")

    try:
        numero = int(input("Informe o número da conta: "))
    except ValueError:
        print("❌ Entrada inválida.")
        return None

    conta = next((c for c in contas_bancarias if c["numero"] == numero), None)

    if not conta:
        print("❌ Conta não encontrada.")
    return conta

# Loop principal do sistema
while True:
    opcao_menu = input("""
    =========================
         SISTEMA BANCÁRIO
    =========================
    [1] Cadastrar Cliente
    [2] Abrir Conta
    [3] Operar Conta
    [4] Sair
    => """)

    if opcao_menu == "1":
        cadastrar_cliente()

    elif opcao_menu == "2":
        abrir_conta()

    elif opcao_menu == "3":
        conta_selecionada = escolher_conta()
        if conta_selecionada:
            while True:
                acao_conta = input("""
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Voltar
    => """)

                if acao_conta == "1":
                    realizar_deposito(conta_selecionada)
                elif acao_conta == "2":
                    realizar_saque(conta_selecionada)
                elif acao_conta == "3":
                    mostrar_extrato(conta_selecionada)
                elif acao_conta == "4":
                    break
                else:
                    print("Opção inválida.")

    elif opcao_menu == "4":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida.")
