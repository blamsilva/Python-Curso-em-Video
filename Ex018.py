print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. ')
from math import sin, cos, tan , radians
a1 = float(input('Digite o valor do ângulo:'))
a = radians(a1)
seno = sin(a)
coseno = cos(a)
tangente = tan(a)
print ('O ângulo {:.2f}º tem o seno de {:.2f}, o coseno de {:.2f} e a tangente de {:.2f}.'.format(a1, seno, coseno, tangente))
