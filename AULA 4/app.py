# sistema escola
alunos = []
medias = []
pergunta =  input('deseja acessar?').lower()
while pergunta == 'sim':
    
    for i in range(3):
        senha = input('senha:')
        if senha == '123':
            print('sistemas de notas..')
            
            nome = input('aluno:' )
            nota1 = float(input('nota matematica: '))
            nota2 = float(input('nota portugues: '))
            nota3 = float(input('nota ingles: '))
            media = (nota1+nota2+nota3) / 3
            print('média', media, 'aluno(a):', nome)
            alunos.append(nome)
            medias.append(media)
            pergunta = input('deseja continuar?')
            if pergunta != 'sim':
                print('***' * 8)
                print('lista de alunos')
                print(aluno)
                print('medias')
                print(media)
                print('***' * 8)
                print('media da sala: ', sum(medias)/len(medias))
                print('***' * 8)
        else:
             print('senha incorreta')
    else:
        print ('senha bloqueada')
        break
    
else:
    print ('até logo')
            
    
            