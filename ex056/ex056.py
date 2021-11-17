#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média
#de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

class Pessoa():
    nome = ''
    idade = None
    sexo = None

    def __init__(self, n, i, s):
        self.nome = n
        self.idade = i
        self.sexo = s

pessoas = list()
somaIdades = 0
mediaIdades = 0
maisVelho = 0
mulheres = 0

for i in range(1, 5):
    print(f'---- {i}ª Pessoa ----')
    nome = input('Nome: ')
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('Entrada inválida, tente novamente!')
        else:
            break
    sexo = str(input('Sexo [M/F]: ').strip().upper())[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Entrada inválida. Digite o sexo [M/F]: ').strip().upper())[0]

    p = Pessoa(nome, idade, sexo)
    pessoas.append(p)

for i in range (0, len(pessoas)):
    somaIdades = somaIdades + pessoas[i].idade

    if pessoas[i].idade > maisVelho:
        maisVelho = pessoas[i].idade
        posicaoMaisVelho = i

    if pessoas[i].sexo == 'F' and pessoas[i].idade < 20:
        mulheres = mulheres + 1

mediaIdades = somaIdades / len(pessoas)

print(f'A média de idade do grupo é {mediaIdades:.1f}.')
print(f'O homem mais velho tem {maisVelho} anos e se chama {pessoas[posicaoMaisVelho].nome}.')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos.')
