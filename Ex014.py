print('Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.')
c = float(input('Digite a temperatura em Graus Célsius:'))
f = ((c*9)/5)+32
print('{:.2f}ºCeusius equivalem a {:.2f}º Fahrenheit.'.format(c, f))