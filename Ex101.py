

print('\033[1:51m Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como '
      'parâmetro o ano de nascimento de uma pessoa,\n retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições. \033[m')

def voto(anonascimento=0):
    from datetime import date
    ano = date.today().year
    anonascimento = int(input("Digite o Ano do seu Nascimento: "))
    idade = ano - anonascimento
    if idade > 16 and idade < 18 or idade > 65:
        return 'Voto Opcional'
    elif idade > 18 and idade <= 65:
       return 'Voto Obrigatório'
    elif idade < 16:
        return 'Voto Negado'

# Programa Principal
print(voto())





