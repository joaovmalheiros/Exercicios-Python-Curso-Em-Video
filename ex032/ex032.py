#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

while True:
    try:
        sYear = input('Que ano quer analisar? Coloque 0 para analisar o atual:')
        iYear = int(sYear)
    except:
        print('Valor inválido! Tente novamente...')
    else:
        break

#Se a entrada for igual a 0, utiliza um objeto da classe date para pegar o ano atual:
if iYear == 0:
    current_date = date.today()
    iYear = current_date.year

#Revisar a lógica do if:
if (iYear % 4 == 0 and iYear % 100 != 0) or iYear % 400 == 0:
    print(f'O ano de {iYear} É BISSEXTO!')
else:
    print(f'O ano de {iYear} NÃO É BISSEXTO!')
