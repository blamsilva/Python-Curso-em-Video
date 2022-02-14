print('\033[1;51m Exercício Python 087: Aprimore o desafio anterior, mostrando no final:\n A) A soma de todos os valores pares digitados.\n B) A soma dos valores da terceira coluna.\n C) O maior valor da segunda linha.\033[m')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Define a lista com 3 listas possuindo 3 elementos cada #
par = terceira = maior = 0 # Define as variáveis #
for l in range(0,3): # para l contagem 3 faca #
    print('='*50) # imprime na tela = 50 vezes #
    for c in range (0,3): # para c contagem 3 faca #
        matriz[l][c] = int(input(f'Digite o item {l} x {c} : '))  # usuário coloca valor na lista matriz dentro da lista [l] item [c]
        if matriz[l][c] % 2 == 0:  #se o item de matriz[l][c] for par faca #
            par += matriz[l][c] # par vai ser igual a par mais o item matriz[l][c]
        if matriz[l][2]:  # se o item pertencente a matriz na linha [l] e coluna [2] faca #
            terceira += matriz[l][2] # terceira vai ser igual a terceira mais soma do item matriz[l][2]
        if matriz [1][c]: #  se o item for da pertecente a matriz na linha [1] e coluna [c] faca #
           if maior < matriz [1][c]: # se maior for menor que o item matriz[1][c] faca #
               maior = matriz [1][c] # maior assume o valor do item matriz[1][c] #
print('=' * 50) # imprime na tela = 50 vezes #
for l in range(0, 3): # para l contagem 3 faca #
    for c in range(0, 3): # para c contagem 3 faca #
        print(f'[{matriz[l][c]:^5}]', end='') #imprime a lista matriz [l] e item [c] centralizado dentro de 5 espaços
    print() # Quebra a linha quando c atinge a contagem máxima #
print('=' * 50 # imprime na tela = 50 vezes #
print(f'A) A Soma de todos os pares é {par}') # imprime a frase e o elemento dentro de format #
print(f'B) A Soma de todos os itens da 3ª Coluna é {terceira}') # imprime a frase e o elemento dentro de format #
print(f'C) O Maior Valor da 2ª linha é {maior}') # imprime a frase e o elemento dentro de format #
