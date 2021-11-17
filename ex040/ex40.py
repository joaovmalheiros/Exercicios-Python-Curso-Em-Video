#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
#de acordo com a média atingida:

while True:
    try:
        n1 = float(input('Digite a primeira nota: '))
        n2 = float(input('Digite a segunda nota: '))
    except:
        print('Entrada inválida, tente novamente...')
    else:
        break

avg = (n1 + n2) / 2
print(f'Tirando {n1} e {n2} a média do aluno é {avg:.1f}')

if avg >= 5 and avg <= 7:
    print('O aluno está de recuperação!')
elif avg > 7:
    print('O aluno está aprovado!')
else:
    print('O aluno está reprovado!')
