from time import sleep
print('\033[1:51m Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com '
      'valores inteiros.\n Seu programa tem que analisar todos os valores e dizer qual deles é o maior. \033[m')

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('\nAnálisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    sleep(0.2)
    print(f'O Maior valor informado foi {maior}')
    sleep(0.2)

# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()