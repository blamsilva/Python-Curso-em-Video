print("\033[1;51m Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.\n Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120 \033[m")
from math import factorial
'''Função para calcular o valor do fatorial'''
n = int(input('Digite um número para calcular seu fatorial:'))
c = n
f = factorial(n)
'''Calcula o valor do fatorial'''
fc = 1
print('O Fatorial de {} é {}'.format(n, f))
print('Calculando {}!'.format(n), end='\n')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fc *= c
    c -= 1
print('{}'.format(f))
print("FIM")
