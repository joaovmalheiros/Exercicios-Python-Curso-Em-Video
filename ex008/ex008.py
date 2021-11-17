#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

while True:
    try:
        smetros = input('Digite um valor em metros: ')
        fmetros = float(smetros)
    except:
        print('Dado inválido!')
    else:
        break

fcentimetros = fmetros * 100
fmilimetros = fmetros * 1000

print(f'A medida de {fmetros} metros corresponde a')
print(f'{fcentimetros} centímetros')
print(f'{fmilimetros} milímetros')
