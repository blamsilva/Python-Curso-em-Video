print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')
km = float(input('Digite a quantidade de Km percorridos:'))
d =  float(input('Digite a quantidade de Dias utilizados:'))
pkm = km*0.15
pd = d*60
pt = pkm + pd
print('{:.2f}Km rodados custaram R${:.2f} e {:.0f} Dias alugados custaram R${:.2f}, totalizando R${:.2f}'.format(km, pkm, d, pd, pt))