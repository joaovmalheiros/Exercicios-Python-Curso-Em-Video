#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

while True:
    try:
        #Colocar entrada em verde:
        velocidade = input('Qual é a velocidade atual do carro? ')
        velocidade = int(velocidade)
    except:
        print('Valor Invalido!Tente novamente...')
    else:
        break

if velocidade > 80:
    multa = (velocidade - 80) * 7
    #Colocar texto em vermelho:
    print('Multado! Você excedeu o limite permitido que é de 80km/h')
    print(f'Você deve pagar uma multa de R${multa}!')

#Colocar texto em amarelo:
print('Tenha um bom dia! Dirija com cuidado!')
