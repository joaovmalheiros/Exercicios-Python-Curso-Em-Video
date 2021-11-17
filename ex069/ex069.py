#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
#perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

def verificaNumero():
    pass

class Pessoa():
    idade = 0
    sexo = None

    def __init__(self, i, s):
        self.idade = i
        self.sexo = s

maiorDeIdade = 0
menorDeVinte = 0
homens = 0
continua = 'S'

listasDePessoas = list()

while continua in 'Ss':

    idade = int(input('Idade: '))
    if idade < 20:
        menorDeVinte = menorDeVinte + 1
        if idade > 18:
            maiorDeIdade = maiorDeIdade + 1
    else:
        maiorDeIdade = maiorDeIdade + 1

    sexo = str(input('Sexo: ')).upper().strip()[0]
    if sexo == 'M':
        homens = homens + 1

    p = Pessoa(idade, sexo)
    listasDePessoas.append(p)



    while True:
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]

        print(continua)

        if continua not in 'Ss' and continua not in 'Nn':
            print('Opção inválida!')
        else:
            break



print(f'Total de pessoas com mais de 18 anos: {maiorDeIdade}.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {menorDeVinte} mulheres com menos de 20 anos.')
