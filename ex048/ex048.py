#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
#no intervalo de 1 até 500.

soma = 0
count = 0

#o último argumento da função range indica que é para pular de dois em dois.
for numero in range(1, 501,2):
    if numero % 3 == 0:
        soma = soma + numero
        count = count + 1

print(f'A soma de todos os {count} valores solicitados é {soma}.')
