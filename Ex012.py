print("Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.")
pa = float(input('Digite o valor do Produto: R$'))
pd = pa * 0.95
print('O Produto de Valor R${:.2f} com desconto de 5% custará R${:.2f}'.format(pa, pd))