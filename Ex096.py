print('Exercício Python 096: Faça um programa que tenha uma função chamada área(), '
      '\nque receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.\n')

def área(l, c):
    a = l * c
    print(f'O terreno de medidas {l} x {c} tem área igual á: {a} m²')


# Programa Principal

print('Calculadora de Área de um terreno retangular')
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno do terreno: '))
área(l, c)
