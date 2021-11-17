# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

while True:
    try:
        ssalario_inicial = input('Qual é o salário do funcionário?')
        fsalario_inicial = float(ssalario_inicial)
    except:
        print('Valor inválido, tente novamente..')
    else:
        break

salario_com_aumento = fsalario_inicial * 1.15

print(f'Um funcionário que ganhava R${fsalario_inicial:.2f}, com 15% de aumento passa \
a receber R${salario_com_aumento:.2f}')
