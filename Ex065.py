print('\033[1;51m Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,\n mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.\n O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores\033[m')
n = int(input('Digite um Valor:'))
maior = n
menor = n
continuar = str(input('Continuar S / N:')).strip().upper()
while continuar not in 'SsNn':
    continuar = str(input('Digite uma opção válida\nContinuar S / N:')).strip().upper()
média = n
cont = 1
soma = n
while continuar == 'S':
    n = int(input('Digite outro Valor:'))
    cont += 1
    soma += n
    média =  soma/cont
    continuar = str(input('Continuar S / N:')).strip().upper()
    while continuar not in 'SsNn':
        continuar = str(input('Digite uma opção válida\nContinuar S / N:')).strip().upper()
print('Foram digitados {:.0f} números ==== O total de suas somas é {:.2f} === a média foi de {:.2f}'.format(cont, soma, média))
