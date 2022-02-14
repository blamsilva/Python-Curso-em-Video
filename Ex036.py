print('Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. \nPergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.\n A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.')
v = float(input('Digite o valor da Casa:\nR$'))
s = float(input('Digite o valor do seu Salário:\nR$'))
a = int(input('Digite o prazo de 1 a 15 anos:\n'))
p = v/(a*12)
if s*.30 >= p:
    print('Sua parcela de R${:.2f} foi aprovada para pagamento em {} meses.'.format(p, a*12))
    print('\033[1;34mEMPRÉSTIMO APROVADO\033[M')
else:
    print('Sua parcela ficou em R${:.2f} está acima do limite permitido de R${:.2f} para seu salário.'.format(p, s*0.3))
    print('\033[1;31mEMPRÉSTIMO NEGADO\033[m')