'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

nomeCompleto = input('Digite seu nome completo: ')
nomeDivido = nomeCompleto.split()

#Dá para utilizar o método count da classe string também
espacos = 0
for i in nomeCompleto:
    if i == ' ':
        espacos = espacos + 1

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nomeCompleto.upper()}')
print(f'Seu nome em minúsculas é {nomeCompleto.lower()}')
print(f'Seu nome tem ao  todo {len(nomeCompleto)-espacos} letras')
print(f'Seu primeiro nome é {nomeDivido[0]} e ele tem {len(nomeDivido[0])} letras')
