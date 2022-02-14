print('\033[1;51m Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única \n que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente \033[m')
num = [[], []] # Cria uma lista com duas listas dentro listas num[0] e num[1]#
n = 0 # variável para digitar os números #
for c in range(0,7): # para c dentro da contagem de 7 faça:
    n = int(input('Digite um valor para adicionar a lista: ')) # input para o usuário definir um valor para n #
    if n % 2 == 0: # se que verifica se o valor de n for par faça #
        num[0].append(n) # adiciona a lista num[0] o número n #
    else: # se não atender a condição anterior então faça #
        num[1].append(n) # adiciona a lista num[1] o número n #
num[0].sort() # organiza a lista num[0] em ordem crescente #
num[1].sort() # organiza a lista num[1] em ordem crescente #
print(f'A Lista par é {num[0]}') # Imprime a frase e a lista indicada pelo format #
print(f'A Lista ímpar é {num[1]}') # Imprime a frase e a lista indicada pelo format #
