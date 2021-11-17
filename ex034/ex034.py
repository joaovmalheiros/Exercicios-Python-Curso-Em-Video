# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

while True:
    try:
        sSalario = input('Qual o salario do funcionario? ')
        salarioAntigo = float(sSalario)
    except:
        print('Valor inválido, tente novamente...')
    else:
        break
if salarioAntigo > 1250:
    salarioNovo = salarioAntigo * 1.10
else:
    salarioNovo = salarioAntigo * 1.15

print(f'Quem ganhava R${salarioAntigo:.2f} passa a ganhar R${salarioNovo:.2f} agora.')
