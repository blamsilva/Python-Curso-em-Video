print('\033[1;51m Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.\n Se o valor digitado for ímpar, desconsidere-o.\033[m')
s = 0
cont = 0
for c in range(0,6):
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        s += n
        cont += 1
print ('Você digitou {} números pares e a soma deles foi de {}'.format(cont, s))