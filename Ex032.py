print('Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.')
from datetime import date
ano = int(input('Digite um ano, coloque 0 se quiser o ano atual:'))
if ano == 0:
    ano = date.today().year
quatro = ano%4
'''A Divisão tem quer ser exta de resto 0'''
cem = ano%100
'''A Divisão não pode ser exata resto diferente de 0'''
quatocentos = ano%400
'''A Divisão tem que ser exata de resto 0'''
if quatro == 0 and cem != 0 or quatocentos == 0:
    print('O Ano {} é Bissexto'.format(ano))
else:
    print('O Ano {} não é Bissexto'.format(ano))
