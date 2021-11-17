#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo: [M/F] ').strip().upper())[0]

while sexo != 'M' and sexo != 'F':
    #Tirar os espaços, colocar em maiúsculas e pegar só a primeira letra da entrada:
    sexo = str(input('Dados inválidos, por favor informe seu sexo: [M/F] ').strip().upper())[0]

print(f'Sexo {sexo} registrado com sucesso!')
