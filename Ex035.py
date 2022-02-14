print('Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.')
l1 = float(input('Digite um lado do triângulo:'))
l2 = float(input('Digite outro lado:'))
l3 = float(input('Digite outro lado:'))
'''Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois
 e maior que o valor absoluto da diferença entre essas medidas.'''
if l1 < (l2+l3) and l2 < l1 + l3 and l3 < l1 + l2:
    print('Podem formar um triângulo')
else:
    print('Não podem formar um triângulo')
