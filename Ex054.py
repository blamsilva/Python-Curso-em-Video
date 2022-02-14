print('\033[1;51m Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.\n No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.\033[m')
from datetime import date
maiores = 0
menores = 0
for c in range(1,8):
    ano = int(input('Digite o ano em que a {}º pessoa nasceu:'.format(c)))
    idade = date.today().year - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('Existem {} menores de idade.'.format(menores))
print('Existem {} maiores de idade.'.format(maiores))