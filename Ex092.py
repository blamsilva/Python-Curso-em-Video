print('\033[1;51m Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. \n Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.\n Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.\033[m')
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] > 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=-='*20)
for k, c in dados.items():
    print(f' - {k} tem o valor {c}')

