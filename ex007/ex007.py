#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

while True:
    try:
        svalue1 = input('Digite a primeira nota:')
        svalue2 = input('Digite a segunda nota:')
        fvalue1 = float(svalue1)
        fvalue2 = float(svalue2)
    except:
        print('Dados inválidos!')
    else:
        break

avg = (fvalue1 + fvalue2) / 2

print(f'A média entre {fvalue1} e {fvalue2} é {avg}')
