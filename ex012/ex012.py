# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

while True:
    try:
        spreco = input('Qual é o preço do produto?')
        fpreco = float(spreco)
    except:
        print('Valor inválido!')
    else:
        break

preco_com_desconto = fpreco * 0.95

print(f'O produto que custava R${fpreco:.2f}, na promoção com desconto \
de 5% vai custar R${preco_com_desconto:.2f}')
