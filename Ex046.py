print('\033[1;51m Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,\n indo de 10 até 0, com uma pausa de 1 segundo entre eles.\033[m')
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1;33;41mSOLTAR FOGOS\033[m')
