print('\033[1;51m Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,'
      '\n guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.'
      '\n No final, mostre:\n A) Quantas pessoas foram cadastradas \n B) A média de idade'
      '\n C) Uma lista com as mulheres'
      '\n D) Uma lista de pessoas com idade acima da média \033[m')
continuar = 'S'
quantidade = 0
cadastro = {}
maiores = []
lista = []
somaidade = 0
media = 0
mulheres = []
print('=' * 40)
while continuar == 'S':
    cadastro['nome'] = str(input('Digite seu Nome: '))
    cadastro['sexo'] = str(input('Sexo: M - Masculino / F - Feminino :')).strip().upper()
    if cadastro['sexo'] not in 'MF':
        cadastro['sexo'] = str(input('ERRO! \nSexo: M - Masculino / F - Feminino :')).strip().upper()
    if cadastro['sexo'] in 'F':
        mulheres.append(cadastro['nome'])
    cadastro['idade'] = int(input('Idade: '))
    quantidade += 1
    somaidade += cadastro['idade']
    if continuar != 'SN':
        continuar = str(input('Deseja continuar? S / N : ')).strip().upper()
    lista.append(cadastro.copy())
print('=' * 40)
media = somaidade / quantidade
print(f'A) Foram cadastradas {quantidade} pessoas')
print(f'B) A média de idades foi de {media}')
print(f'C) As Mulheres cadastradas Foram: {mulheres}')
for c in lista:
    if c['idade'] > media:
        maiores.append(c['nome'])
print(f'D) As Pessoas Acima da média de idade são: {maiores} ')
print(lista)
