#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


while True:
    try:
        slargura = input('Digite a largura da parede: ')
        saltura = input('Digite a altura da parede: ')
        flargura= float(slargura)
        faltura = float(saltura)
    except:
        print('Dados inválidos!')
    else:
        break

area = flargura * faltura
litros = area / 2

print(f'Sua parede tem dimensao de {flargura}x{faltura} e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {litros}l de tinta')
