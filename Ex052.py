print('\033[1;51m Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.\033[m')
n = int(input('Digite um númere e descubra se ele é primo: '))
cont = 0
for c in range(n,0,-1):
    if n % c == 0:
        print('O Número é divisivel por:')
        print(c)
        cont += 1
if cont == 2:
    print('O NÚMERO É PRIMO')
else:
    print('O NÚMERO NÃO É PRIMO')
