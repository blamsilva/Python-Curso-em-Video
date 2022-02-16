print('\033[1;51m Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.'
      'Depois disso, mostre:\n A) Quantos números foram digitados.\n B) A lista de valores, ordenada de forma decrescente.'
      '\n C) Se o valor 5 foi digitado e está ou não na lista.\033[m')

n = 0
lista = []
while n != 999:
    n = int(input('Digite um valor ou digite 999 para sair: '))
    if n != 999:
        lista.append(n)
print('-----'*30)
print(f'A) Foram Digitados {len(lista)} números')
reverselista = lista[:]
reverselista.sort(reverse=True)
print(f'B) A lista em valores decrescentes: {reverselista}')
if 5 in lista:
    print(f'C) O Valor 5 está na Lista')
else:
    print('C) O Valor 5 não está na Lista')

print(lista)