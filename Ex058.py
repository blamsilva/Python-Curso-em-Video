print('\033[1;51m Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. \n Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.\033[m')
from random import randint
from time import sleep
print("-*--*-"*25)
pc = randint(0, 10)
n = int(input('Digite um número de entre 0 e 10 e tente adivinhar o que o pc escolheu.\n:'))
cont = 0
while not n == pc:
    cont += 1
    if n < pc:
        palavra = 'Maior'
    else:
        palavra = 'Menor'
    n = int(input('{}, Não foi dessa vez, escolha outro número:'.format(palavra)))
print('Parabéns você acertou depois de {} tentativas, o número que o pc escolheu foi o {}'.format(cont,pc))
print("FIM")