'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
#Biblioteca e classe utilizadas para conseguir saber o ano atual:
from datetime import date

while True:
    try:
        anoDeNascimento = int(input('Ano de nascimento: '))
    except:
        print('Entrada inválida, digite um valor inteiro!')
    else:
        break

dataAtual = date.today().year
idade = dataAtual - anoDeNascimento

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
