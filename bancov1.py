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
        valor = float(input("Insira o valor a ser depositado? "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("O Valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Você não tem saldo suficiente')
        elif excedeu_limite:
            print('Limite excedido')
        elif excedeu_saques:
            print("Numero maximo de saques excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print('Por Favor, informe um valor valido')
    
    elif opcao == "e":
        
        print("\n================ EXTRATO ===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================================")

    elif opcao == "q":
        break

    else:
        print('Opção invalida, por favor selecione novamente a opção desejada')
