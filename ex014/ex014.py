#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
while True:
    try:
        sCelsius = input('Informe a temperatura em ºC:')
        fCelsius = float(sCelsius)
    except:
        print('Valor inválido, tente novamente...')
    else:
        break

fFarenheit = (fCelsius * 1.8) + 32

print(f'A temperatura de {fCelsius:.1f}ºC corresponde a {fFarenheit:.1f}ºF!')
