'''
Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''


print('-'*40)
print('LOJA SUPER BARATÃO')
print('-'*40)

total = contador = maisBarato = 0
nomeMaisBarato = None

while True:
    nomeDoProduto = str(input('Nome do Produto: '))
    valorDoProduto = int(input('Preço: R$'))

    total = total + valorDoProduto

    if valorDoProduto > 1000:
        contador =  contador + 1

    if nomeMaisBarato is None:
        maisBarato = valorDoProduto
        nomeMaisBarato = nomeDoProduto
    elif valorDoProduto < maisBarato:
        maisBarato = valorDoProduto
        nomeMaisBarato = nomeDoProduto


    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N]').upper().strip()[0]
    if resposta == 'N':
        break

print('-'*15, end='')
print('FIM DO PROGRAMA', end='')
print('-'*15)
print(f'O total da compra foi R${total}')
print(f'Temos {contador} custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMaisBarato} que custa R${maisBarato}')
