
def cadastro():
    nome = input('digite o seu nome: ')
    email = input('digite o seu email: ')
    idade = int(input('digite a sua idade: '))
        
    print('\n--- Cadastro realizado ---')
    print('nome: ', nome)
    print('email', email)
    print('idade', idade)

quantidade = int(input('quantas pessoas deseja cadastrar?: '))
for i in range (quantidade):
        print('\nCadastro', i + 1)



continuar = 's'
while continuar == 's':
    print('\n=== Sistema de cadatro===')
    
    cadastro()
    
    continuar = input('\nDeseja cadastrar outra pessoa? (s/n):').lower()

else:
    print('\nSistema encerrado!')

continuar()