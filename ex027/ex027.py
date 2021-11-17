#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
#o primeiro e o último nome separadamente

nome = input('Digite seu nome completo: ')

nomeDividido = nome.split()

if(len(nomeDividido) < 1):
    print('Nenhum nome foi digitado!')
else:
    print('Muito prazer em te conhecer!')
    print(f'Seu primeiro nome é {nomeDividido[0]}')
    if(len(nomeDividido) > 1):
        print(f'Seu último nome é {nomeDividido[len(nomeDividido)-1]}')
