print("\033[1;51m Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.\n O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:\n A) qual é o total gasto na compra.\n B) quantos produtos custam mais de R$1000. \n C) qual é o nome do produto mais barato. \033[m")
print("=="*10)
print("  ROTA BIKE PEÇAS")
print("=="*10)
tot = mil = preço = 0
nmenor = nomep = 'nenhum'
pmenor = 9999999999999
while True:
    nomep = str(input('Digite o nome do produto:'))
    preço = float(input('Digite o preço do produto:'))
    tot = tot + preço
    if preço > 1000:
        mil += 1
    if preço < pmenor:
        nmenor =  nomep
        pmenor = preço
    cont = str(input('DESEJA CONTINUAR: S /N :')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('OPÇÃO INVÁLIDA\nDESEJA CONTINUAR: S /N :')).strip().upper()[0]
    if cont == 'N':
        break
print (f'A) O Total foi de R$ {tot:.2f}\nB) ({mil}) Produtos mais caros que R$ 1.000,00\nC) {nmenor.capitalize()} é o produto mais barato que custa R$ {pmenor:.2f}')


