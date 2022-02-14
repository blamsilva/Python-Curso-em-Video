n = int(input('Digite um valor:'))
if n >=10:
    print('Foi Maior que 09.')
else:
    print('Foi menor que 10')
print('FIM')
'''-----------------------------------------------'''
tempo = int(input('Digite a idade do carro:'))
if tempo <=3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('FIM')
'''-----------------------------------------------'''
print('CARRO NOVO' if tempo <= 3 else 'CARRO VELHO')
print('Fim')