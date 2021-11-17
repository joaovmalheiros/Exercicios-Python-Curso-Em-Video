#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

lst = [0, 0, 0]
count = 0

for l in lst:
    while True:
        try:
            sValue = input(f'Digite o valor do {count+1}º valor: ')
            lst[count] = float(sValue)
        except:
            print('Valor inválido! Tente novamente...')
        else:
            count = count + 1
            break
lst.sort()

print(f'O menor valor digitado foi {lst[0]}')
print(f'O maior valor digitado foi {lst[2]}')

#Fazer novamente sem utilizar a classe list
