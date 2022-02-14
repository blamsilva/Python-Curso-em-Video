print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados')
a = float(input('Digite a altura da Parede:'))
l = float(input('Digite a largura da Parede:'))
m2 = a*l
ln = m2/2
print('Para pintar uma Parede de Altura {:.2f}m e Largura {:.2f}m com {:.2f} m².\nSão necessários {:.2f} litros de tinta.'.format(a, l, m2, ln))