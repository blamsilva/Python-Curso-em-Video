print('Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta\ne mostre sua categoria, de acordo com a idade:\n– Até 9 anos: MIRIM\n– Até 14 anos: INFANTIL\n– Até 19 anos: JÚNIOR\n– Até 25 anos: SÊNIOR\n– Acima de 25 anos: MASTER')
from datetime import date
nasc = int(input('Digite o ano do seu nascimento:'))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('Você tem {} anos e Sua categoria é MIRIN'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e Sua categoria é INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos e Sua categoria é JÚNIOR'.format(idade))
elif idade > 19 and idade <= 25:
    print('Você tem {} anos e Sua categoria é SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e Sua categoria é MASTER'.format(idade))
