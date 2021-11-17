#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

svalue = input('Quanto dinheiro voce tem na carteira?')

aux = True
while aux == True:
    try:
        fvalue = float(svalue)
        aux = False
    except:
        print('Dado inválido!')

dolarValue = fvalue / 4.96

print(f'Com R${fvalue} você pode comprar US${dolarValue:.2f}')

#Procurar se tem alguma forma de conseguir o valor corrente do dólar
