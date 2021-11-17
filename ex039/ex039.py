#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
#do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

while True:
    try:
        anoDeNascimento = int(input('Ano de Nascimento: '))
    except:
        print('Entrada inválida, tente novamente!')
    else:
        break
#Colocar restrição para pessoa não digitar valores numéricos inválidos!!!

currentDate = date.today()
idade = currentDate.year - anoDeNascimento

print(f'Você tem {idade} anos!')

if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    print(f'Ainda falta {18 - idade} anos para o alistamento.')
else:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {currentDate.year - (idade - 18)}.')
