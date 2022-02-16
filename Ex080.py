print('\033[1;51m Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos \n'
      ' e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).'
      '\n No final, mostre a lista ordenada na tela \033[m')

lista = []
for c in range(0, 5): # Para Fazer a leitura de 5 valores
    n = int(input('Digite um valor: ')) # Comando para digitar um valor inteiro
    if c == 0 or n > lista[-1]: 
        lista.append(n)
        print('Adicionado ao final da Lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} na lista.')
                break
            pos += 1
print('---'*30)
print(f'Os Valores digitados em ordem foram {lista}')






