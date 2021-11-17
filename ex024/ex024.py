#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input('Em que cidade você nasceu? ')

#Usar função split() para tirar os espaços:
cidade = cidade.split()

print(cidade[0].upper() == 'SANTO')
