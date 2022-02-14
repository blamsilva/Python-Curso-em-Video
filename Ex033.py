print('Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')
n1 = float(input('Digite um Número:'))
n2 = float(input(('Digite outro Número:')))
n3 = float(input(('Digite outro Número:')))
maior = 99999999
menor = 0
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
if n3 > n1 and n3 > n2:
    maior = n3
else:
    maior = maior
if n3 < n2 and n3 < n1:
    menor = n3
else:
    menor = menor
print('O Maior número é {:.2f}'.format(maior))
print('O Menor número é {:.2f}'.format(menor))
