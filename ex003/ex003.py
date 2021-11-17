#Crie um programa que leia dois números e mostre a soma entre eles.

while True:
    try:
        sValue1 = input('Digite o primeiro número:')
        sValue2 = input('Digite o segundo número:')
        fValue1 = float(sValue1)
        fValue2 = float(sValue2)
    except:
        print('Digite apenas valores numéricos!')
    else:
        break

print(f'A soma entre {fValue1} e {fValue2} é {fValue1 + fValue2}')
