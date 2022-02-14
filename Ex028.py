print('Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5\n e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.\n O programa deverá escrever na tela se o usuário venceu ou perdeu.')
from random import randint
from time import sleep
print("-*--*-"*25)
pc = randint(0, 5)
n = int(input('Digite um valor entre 0 e 5 e tente adivinhar o que o pc escolheu:'))
print("Processando")
sleep(3)
'''o método sleep faz o computador esperar por segundos determinados para continuar'''
print('Parabés você acertou!'if pc == n else 'Você errou')
print('Seu número foi {} e o número do pc foi {}'.format(n, pc))
