print('Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.\n Para salários superiores a R$1250,00, calcule um aumento de 10%.\n Para os inferiores ou iguais, o aumento é de 15%.')
s = float(input('Digite seu salário e veja o aumento dado:'))
if s > 1250:
    sn = s * 1.10
    taxa = 10
else:
    sn = s * 1.15
    taxa = 15
print('Seu salário de R${:.2f} teve um aumento de {:.0f}% e passou a ser R${:.2f}'.format(s, taxa, sn))
print('FIM')
