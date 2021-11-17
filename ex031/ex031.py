# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

while True:
    try:
        distancia = input('Qual é a distância da sua viagem (digite em km)? ')
        distancia = float(distancia)
    except:
        print('Valor inválido, tente novamente!')
    else:
        break

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print(f'Você está prestes a começar uma viagem de {distancia}km')
print(f'E o preço da sua passagem será de R$ {passagem:.2f}!')
