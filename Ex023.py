print('Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.')

num = int(input('Digite um número de 1 a 9999:\n'))
u = num//1%10
print('Analisando o número {}'.format(num))
print('{} Unidades '.format(u))
d = num//10 %10
print('{} Dezenas'.format(d))
c = num//100%10
print('{} Centenas'.format(c))
m = num//1000%10
print('{} Milhares'.format(m))
