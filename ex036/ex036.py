# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da
#casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
#do salário ou então o empréstimo será negado.

while True:
    try:
        valorDaCasa = float(input('Valor da casa: '))
        salarioDoComprador = float(input('Salário do comprador: '))
        anosDeFinanciamento = int(input('Quantos anos de financiamento? '))
    except:
        print('Você digitou algum valor inválido, tente novamente!')
    else:
        break

#Prestação mensal é igual à prestação anual dividida por 12 meses:
prestacaoMensal = (valorDaCasa / anosDeFinanciamento) / 12

print(f'Para pagar uma casa R${valorDaCasa:.2f} em {anosDeFinanciamento} anos a prestação\
será de R${prestacaoMensal:.2f} ')

if prestacaoMensal > (salarioDoComprador * 0.3):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONDEDIDO!')
