import datetime

def menu():
    menu = """\n
    ================ MENU ================
    [d] DEPOSITAR
    [s] SACAR
    [e] EXTRATO
    [nc] NOVA CONTA
    [lc] LISTAR CONTAS
    [nu] NOVO USUÁRIO
    [q] SAIR
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            data_corrente = datetime.datetime.now()
            data_operacao = data_corrente.strftime('%d/%m/%Y %H:%M:%S')
            extrato += f'DEPÓSITO: R$ {valor:.2f} - {data_operacao}\n'
    else:
        print('\nFALHA NA OPERAÇÃO! VALOR INVÁLIDO!')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excede_saldo = valor > saldo
    excede_limite = valor > limite
    excede_saques = numero_saques >= limite_saques

    if excede_saldo:
        print('\nFALHA NA OPERAÇÃO. SALDO INSUFICIENTE!')

    elif excede_limite:
        print("\nFALHA NA OPERAÇÃO. VALOR DO SAQUE EXCEDE LIMITE!")

    elif excede_saques:
        print("\nFALHA NA OPERAÇÃO. NÚMERO MÁXIMO DE SAQUES EXCEDIDO!")

    elif valor > 0:
        saldo -= valor
        data_corrente = datetime.datetime.now()
        data_operacao = data_corrente.strftime('%d/%m/%Y %H:%M:%S')
        extrato += f"SAQUE: R$ {valor:.2f} - {data_operacao}\n"
        numero_saques += 1

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("NÃO HÁ MOVIMENTAÇÕES!." if not extrato else extrato)
    print(f"\nSALDO: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("INFORME O CPF (APENAS DÍGITOS): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n++++++++++ CPF JÁ CADASTRADO! ++++++++++")
        return

    nome = input("INFORME O NOME: ")
    data_nascimento = input("INFORME A DATA DE NASCIMENTO (dd/mm/aaaa): ")
    endereco = input("INFORME O ENDEREÇO COMPLETO: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("++++++++++ USUÁRIO CRIADO COM SUCESSO! ++++++++++")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("INFORME O CPF DO USUÁRIO: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== CONTA CRIADA COM SUCESSO! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n++++++++++ FALHA NA OPERAÇÃO. USUÁRIO NÃO ENCONTRADO! ++++++++++")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input('\nDIGITE O VALOR PARA DEPÓSITO: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input('\nDIGITE O VALOR PARA SAQUE: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\nOPÇÃO INVÁLIDA! INFORME NOVAMENTE A OPÇÃO!")


main()
