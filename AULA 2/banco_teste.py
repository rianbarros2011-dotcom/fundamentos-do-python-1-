
saldo = 5000.20
senha = 1234
print('banco z...')
print('seja bem vindo(a)')
senha = int(input(' digite sua senha: '))
op = input('''escolha a operação
            1 - saque
            2 - deposito
            3 - extrato

''')
resultado = op == '1' and float(input('voce escolheu saque R$:')) - saldo or op == '2' and float(input('voce escolheu deposito')) + saldo or op == '3' ('voce escolhe um extrato')
print(resultado)
