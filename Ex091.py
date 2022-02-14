print('\033[1;51m Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.\n No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.\033[m')
from random import  randint # importa o método para gerar números aleatórios
from time import sleep #importa o método para da um tempo de pausa no programa
from operator import itemgetter # importa a função que ordena o dicionário por determinada chave
jogo = {'jogador 1': randint(1,6), #jogo é um dicionário que contém 4 jogadores com 4 números aleatórios sorteado pelo randit
        'jogador 2': randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)}
ranking = list() # determina ranking como uma lista vazia
print('Valores Sorteados:') # imprime a frase
for k, v in jogo.items(): # condicional para imprimir para cada chave valores.
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # dentro de jogo.items itemgetter coloca em ordem crescente, o reverse = True coloca em ordem inversa (do maior para o menor).
print('=-'*20)
print('  == Ranking dos Jogadores ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar {v[0]} com {v[1]}')