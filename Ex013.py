print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.')
s = float(input('Digite o valor do seu salário: R$'))
sn = s*1.15
print('O Sálário antigo de R${:.2f} com um aumento de 15% ficará R${:.2f}'.format(s, sn))