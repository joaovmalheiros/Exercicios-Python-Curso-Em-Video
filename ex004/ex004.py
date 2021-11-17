#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

svalue = input('Digite algo:')
print('O tipo primitivo desse valor é ', type(svalue))
print('Só tem espaços?', svalue.isspace())
print('É um número? ', svalue.isnumeric())
print('É alfabético? ', svalue.isalpha())
print('É alfanumérico? ', svalue.isalnum())
print('Está em maiúsculas? ', svalue.isupper())
print('Está em minúsculas?', svalue.islower())
print('Está capitalizado?', svalue.istitle())
