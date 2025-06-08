from abc import ABC, abstractmethod
from datetime import datetime


class Usuario:
    def __init__(self, localizacao):
        self.localizacao = localizacao
        self.contas_vinculadas = []

    def executar_operacao(self, conta, operacao):
        operacao.processar(conta)

    def vincular_conta(self, conta):
        self.contas_vinculadas.append(conta)


class PessoaFisicaUsuario(Usuario):
    def __init__(self, nome_completo, nascimento, cpf, localizacao):
        super().__init__(localizacao)
        self.nome_completo = nome_completo
        self.nascimento = nascimento
        self.cpf = cpf


class ContaBancaria:
    def __init__(self, id_conta, usuario):
        self._valor_saldo = 0
        self._id_conta = id_conta
        self._codigo_agencia = "0001"
        self._usuario = usuario
        self._log_operacoes = RegistroOperacoes()

    @classmethod
    def criar_conta(cls, usuario, id_conta):
        return cls(id_conta, usuario)

    @property
    def saldo(self):
        return self._valor_saldo

    @property
    def id_conta(self):
        return self._id_conta

    @property
    def codigo_agencia(self):
        return self._codigo_agencia

    @property
    def usuario(self):
        return self._usuario

    @property
    def log_operacoes(self):
        return self._log_operacoes

    def debitar(self, valor):
        if valor <= 0:
            print("\n@@@ Falha: Valor inválido para débito. @@@")
            return False

        if valor > self.saldo:
            print("\n@@@ Falha: Saldo insuficiente. @@@")
            return False

        self._valor_saldo -= valor
        print("\n=== Débito efetuado com sucesso! ===")
        return True

    def creditar(self, valor):
        if valor <= 0:
            print("\n@@@ Falha: Valor inválido para crédito. @@@")
            return False

        self._valor_saldo += valor
        print("\n=== Crédito efetuado com sucesso! ===")
        return True


class ContaCorrenteEspecial(ContaBancaria):
    def __init__(self, id_conta, usuario, limite_credito=500, max_operacoes=3):
        super().__init__(id_conta, usuario)
        self.limite_credito = limite_credito
        self.max_operacoes = max_operacoes

    def debitar(self, valor):
        saques_realizados = len(
            [op for op in self.log_operacoes.historico if op["tipo"] == OperacaoSaque.__name__]
        )

        if valor > self.limite_credito:
            print("\n@@@ Falha: Valor excede o limite permitido. @@@")
        elif saques_realizados >= self.max_operacoes:
            print("\n@@@ Falha: Limite de operações atingido. @@@")
        else:
            return super().debitar(valor)

        return False

    def __str__(self):
        return f""
