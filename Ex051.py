print('\033[1;51m Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.\n No final, mostre os 10 primeiros termos dessa progressão.\033[m')
vi = int(input('Digite um valor inicial:'))
ra = int(input('Digite a Razão:'))
for c in range(vi ,vi+ra*10, ra):
    print(c, end= ' => ')
print('FIM')
