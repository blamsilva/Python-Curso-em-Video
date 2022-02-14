from random import randint
print("\033[1;51m Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.\n Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.\033[m")
lista = randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100)
print ('Os valores sorteados foram :',lista)
#maior = 0
#menor =11
#for l in lista:
#    if l > maior:
#        maior = l
#   elif l < menor:
#        menor = l
print(f'O Maior número é {max(lista)}')#max() - função que busca o maior dentro da tupla
print(f'O Menor número é {min(lista)}')#min() - funcao que busca o menor dentro da tupla
