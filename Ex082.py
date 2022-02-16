print('\033[1;51m Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.'
      '\n Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,'
      '\n respectivamente. Ao final, mostre o conteúdo das três listas geradas. \033[m')

lista = []
pares = []
impares = []
n = 0

while n != 999:
    n = int(input('Digite 999 para sair ou Digite um número: '))
    if n != 999:
        lista.append(n)
        if n % 2  == 0:
            pares.append(n)
        else:
            impares.append(n)
print('----'*30)
print(f'Os Números digitados foram {lista}')
print(f'Os Números pares digitados foram {pares}')
print(f'Os Números ímpares digitados foram {impares}')
