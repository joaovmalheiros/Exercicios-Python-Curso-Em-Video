#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

listaDeAlunos = list()

for x in range(0,4):
    nam = input(f'{x+1}º aluno: ')
    listaDeAlunos.append(nam)

escolhido = random.choice(listaDeAlunos)
print(f'O aluno(a) escolhido foi {escolhido}')

#Sem utilizar a função choice:
#escolha = random.randint(0, 3)
#print(f'O aluno(a) escolhido(a) foi {listaDeAlunos[escolha]}')
