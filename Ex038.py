print('Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:\nO primeiro valor é maior\nO segundo valor é maior\nNão existe valor maior, os dois são iguais')
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
if n1 > n2:
   print('o Primeiro número é maior.')
elif n2 > n1:
    print('O Segundo número é maior')
else:
    print('Não existe maior, os dois números são iguais.')