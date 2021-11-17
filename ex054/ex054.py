#: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
#não atingiram a maioridade e quantas já são maiores.
from datetime import date

idades = list()
anoAtual = date.today().year
maioresDeIdade = 0
menoresDeIdade = 0

for i in range(1, 8):
    while True:
        try:
            anoDeNascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
        except:
            print('Dados inválidos, tente novamente.')
        else:
            idade = anoAtual - anoDeNascimento
            idades.append(idade)
            if idade >= 18:
                maioresDeIdade = maioresDeIdade + 1
            else:
                menoresDeIdade = menoresDeIdade + 1
            break

print(f'Ao todo tivemos {maioresDeIdade} pessoas maiores de idade.')
print(f'E também tivemos {menoresDeIdade} pessoas menores de idade.')
