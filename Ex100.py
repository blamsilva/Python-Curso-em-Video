from random import randint
from time import sleep

print('\033[1:51m Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções '
      '\n chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista  '
      '\n e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.\033[m')

def sorteia(lista):
    print('Sorteando 5 Valores da Lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('Pronto!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

números = list()
sorteia(números)
somaPar(números)
