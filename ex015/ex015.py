#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
#de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
#e R$0,15 por Km rodado.

while True:
    try:
        sDiasAlugados = input('Quantos dias alugados?')
        sKmPercorridos = input('Quantos km rodados?')
        iDiasAlugados = int(sDiasAlugados)
        fKmPercorridos = float(sKmPercorridos)
    except:
        print('Dados inválidos! Tente novamente...')
    else:
        break

total = (60 * iDiasAlugados) + (0.15 * fKmPercorridos)

print(f'O valor a pagar é de R${total:.2f}')
