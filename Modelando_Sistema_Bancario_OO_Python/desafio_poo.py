class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def cadastrar_conta(self, numero):
        conta = Conta(self, numero)
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._agencia = "0001"
        self._historico = []

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self.cliente

    @property
    def agencia(self):
        return self.agencia

    def depositar(self, valor):

        if valor > 0:
            self._saldo += valor
            self._historico.append(f"DEPÓSITO: R${valor}")
            print("\nSAQUE REALIZADO COM SUCESSO!")
            return True
        else:
            print("\nFALHA NA OPERAÇÃO! VALOR INVÁLIDO!")
            return False

    def sacar(self, valor):

        if valor >= self._saldo:
            print("\nSAQUE REALIZADO COM SUCESSO!")
            return True

        elif self._saldo <= 0:
            print("\nFALHA NA OPERAÇÃO. SALDO INSUFICIENTE!")

        else:
            print("\nFALHA NA OPERAÇÃO. VALOR INVÁLIDO!")
        return False

    def listar_historico(self):
        print("\nHISTÓRICO DE OPERAÇÕES:")
        for operacao in self._historico:
            print(operacao)


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """


def main():
    pass


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    conta = Conta.nova_conta(cliente, numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")


main()
