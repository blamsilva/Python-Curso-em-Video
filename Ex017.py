print('Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.\n Calcule e mostre o comprimento da hipotenusa.')
from math import hypot
x = float(input('Digite o valor do cateto oposto:'))
y = float(input('Digite o valor do cateto adjacente:'))
h = hypot(x, y)
print('Um triângulo com o cateto oposto {} e cateto adjacente {} tem a hipotenusa de {:.2f}'.format(x, y, h))
