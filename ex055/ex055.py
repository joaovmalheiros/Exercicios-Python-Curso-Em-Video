#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = list()

for i in range(1, 6):
    while True:
        try:
            peso = float(input(f'Peso da {i} pessoa:'))
        except:
            print('Valor inválido, tente novamente.')
        else:
            pesos.append(peso)
            break

print(f'O maior peso lido foi de {max(pesos)}kg.')
print(f'O menos peso lido foi de {min(pesos)}kg.')

#Fazer sem utilizar a classe list
