'''tupla = variável que guarda város valores identificados por indices'''
lanche = 'Haburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
print('EXEMPLO 1')
print(lanche[2])
print('='*20)
print('EXEMPLO 2')
print(lanche[1:3])
print('='*20)
print('EXEMPLO 3')
print(lanche[1:])
print('='*20)
print('EXEMPLO 4')
print(lanche[-2])
print('='*20)
print('EXEMPLO 5')
print(len(lanche))
print('='*20)
print('EXEMPLO 6')
for c in lanche:
    print(c)
print('Exemplo 7')
'''Tuplas São Imutáveis, uma vez definida ela não pode ser alerada'''
print('EXEMPLO 8')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('EXEMPLO 9')
for cont in range(0, len(lanche)):
    print(cont)
print('EXEMPLO 10')
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('EXEMPLO 11')
for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} está na posição {cont}')
print('EXEMPLO 12')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('EXEMPLO 13')
print(sorted(lanche))#coloca em ordem 





