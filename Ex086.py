print('\033[1;51m Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.\n No final, mostre a matriz na tela, com a formatação correta.\033[m')
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]] # Define a lista com 3 listas possuindo 3 elementos cada #
for l in range(0, 3): # para l contagem 3 faca #
    print('='*50) # imprime na tela = 50 vezes #
    for c in range(0, 3): # para c contagem 3 faca #
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) # usuário coloca valor na lista matriz dentro da lista [l] item [c]
for l in range(0, 3): # para l contagem 3 faca #
    for c in range(0, 3): # para c contagem 3 faca #
        print(f'[{matriz[l][c]:^5}]', end='') #imprime a lista matriz [l] e item [c] centralizado dentro de 5 espaços
    print() # Quebra a linha quando c atinge a contagem máxima #
