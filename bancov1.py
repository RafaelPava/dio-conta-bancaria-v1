menu = '''
************************
Bem vindo ao Banco Pavão

[D] - Depósito
[S] - Saque
[E] - Extrato
[Q] - Sair

O que deseja fazer?
************************

'''

saldo = 1500.00
LIMITE_SAQUES_DIARIOS = 3
saques_realizados = 0
LIMITE_SAQUE = 500.00
extrato = []
saldo_temporario = []

while True:
    print(menu)

    opcao = input('Escolha uma opção: ').upper()
    if opcao == 'D':

        valor_deposito = float(input('Informe o valor do depósito: '))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f'Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}')
            extrato.append(f'Depóstio: R$ {valor_deposito:.2f}')
            saldo_temporario.append(f'{saldo:.2f}')
        else:
            print('Valor de depósito inválido.')

    elif opcao == 'S':
        
        if saques_realizados < LIMITE_SAQUES_DIARIOS:
            valor_saque = float(input('Informe o valor do saque: '))
            if 0 < valor_saque <= LIMITE_SAQUE and valor_saque <= saldo:
                saldo -= valor_saque
                saques_realizados += 1
                print(f'Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}')
                extrato.append(f'Saque: R$ {valor_saque:.2f}')
                saldo_temporario.append(f'{saldo:.2f}')
            elif valor_saque <= 0:
                print('Valor de saque inválido!')
            elif valor_saque > LIMITE_SAQUE:
                print(f'Valor de saque excede o limite de R$ {LIMITE_SAQUE:.2f}.')
            elif valor_saque > saldo:
                print('Saldo insuficiente para realizar o saque.')     
            else:
                print('Valor inválido.')
        else:
            print('Limite de saques diários atingido.')

    elif opcao == 'E':
        i = 0
        for extrato_item in extrato:
            print(f'{extrato_item} ------- Saldo: R${saldo_temporario[i]}')
            print(f'')
            i += 1
        print(f'Saldo atual: R$ {saldo:.2f}')

    elif opcao == 'Q':
        break

    else:
        print('Opção inválida. Escolha novamente')