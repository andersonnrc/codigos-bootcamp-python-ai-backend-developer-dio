menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input('\nDIGITE O VALOR PARA DEPÓSITO: '))

        if valor > 0:
            saldo += valor
            extrato += f'DEPÓSITO: R$ {valor:.2f}\n'
        else:
            print('\nFALHA NA OPERAÇÃO! VALOR INVÁLIDO!')

    elif opcao == "s":
        valor = float(input('\nDIGITE O VALOR PARA SAQUE: '))

        excede_saldo = valor > saldo
        excede_limite = valor > limite
        excede_saques = numero_saques >= LIMITE_SAQUES

        if excede_saldo:
            print('\nFALHA NA OPERAÇÃO. SALDO INSUFICIENTE!')

        elif excede_limite:
            print("\nFALHA NA OPERAÇÃO. VALOR DO SAQUE EXCEDE LIMITE!")

        elif excede_saques:
            print("\nFALHA NA OPERAÇÃO. NÚMERO MÁXIMO DE SAQUES EXCEDIDO!")

        elif valor > 0:
            saldo -= valor
            extrato += f"SAQUE: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("NÃO HÁ MOVIMENTAÇÕES!." if not extrato else extrato)
        print(f"\nSALDO: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("\nOPÇÃO INVÁLIDA! INFORME NOVAMENTE A OPÇÃO!")