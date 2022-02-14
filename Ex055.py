print('\033[1;51m Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.\n No final, mostre qual foi o maior e o menor peso lidos.\033[m')
maior = 0
menor = 10**9
for p in range(1, 6):
    peso = float(input('Digite o Peso da Pessoa {}:'.format(p)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('\nO Maior peso foi o de {}Kg\nO Menor peso foi o de {}Kg'.format(maior, menor))
