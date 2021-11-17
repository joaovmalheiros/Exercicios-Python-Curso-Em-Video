'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

while True:
    try:
        valor = float(input('Preço das compras: R$'))
        print('FORMAS DE PAGAMENTO')
        print('[ 1 ] à vista dinheiro/cheque')
        print('[ 2 ] à vista cartão')
        print('[ 3 ] 2x no cartão')
        print('[ 4 ] 3x ou mais no cartão')
        opcao = int(input('Qual é a opção? '))
    except:
        print('Valor inválido, tente novamente!')
    else:
        break

if opcao == 1:
    novoValor = valor * 0.90
elif opcao == 2:
    novoValor = valor * 0.95
elif opcao == 3:
    novoValor = valor
else:
    while True:
        try:
            parcelas = int(input('Quantas parcelas? '))
        except:
            print('Digite um valor válido!!!')
        else:
            break
    novoValor = valor * 1.20
    print(f'Sua compra será parcelada em {parcelas}x de R${novoValor/parcelas} COM JUROS.')

print(f'Sua compra de R${valor:.2f} vai custar R${novoValor:.2f} no final.')
