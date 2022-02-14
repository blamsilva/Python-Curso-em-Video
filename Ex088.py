print('\033[1;51m Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.\n O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.\033[m')
from random import randint # Importa a função randit para sorteiar números #
from time import sleep # importa a função sleep para dar uma pausa de segundos antes de continuar #
lista = list() # declara a lista lista #
jogos = list() # declara a lista jogos #
print('='*30) # Imprime na tela #
print(f'{"Jogar Na Mega Sena":^30}') # Imprime na tela #
print('='*30) # Imprime na tela #
quant = int(input('Quantos jogos você quer gerar: ')) # Imprime na tela e pede pro usuário digitar uma valor inteiro #
tot = 0 # Declara a variavel tot #
print('='*30) # Imprime na tela #
while tot <= quant: # enquanto tot for menor ou igual a quant faça #
    cont = 0 # declara cont #
    while True: # enquanto for verdade faça #
        num =  randint(1,60) # num é sorteado entre 1 e 60 #
        if num not in lista: # se num não estiver na lista faça #
            lista.append(num) # acrescenta num na lista #
            cont += 1 # faz cont é igual a cont + 1 #
        if cont >= 6: # se cont for maior ou igual a 6 faça #
            break # pare #
    tot += 1 # faz tot é igual a tot + 1 #
    lista.sort() # Ordena lista em ordem crescente #
    if lista not in jogos:
        jogos.append(lista[:]) # acrecenta a lista lista dentro de outra lista jogos
        lista.clear() # limpa a lista #
for c in range(0 , quant): # para c dentro da contagem 0 até quant faça #
    print(f'{c+1}º -  {jogos[c]}') # Imprime cada item da lista jogos
    sleep(0.01) # espera o segundos determinados para prosseguir #
print(f'{"< Boa Sorte! >":^30}') # Imprime na tela #
