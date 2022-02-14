print("\033[1;51m Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.\n No final, mostre uma listagem de preços, organizando os dados em forma tabular.\033[m")
prod = ('Lápis', 1.75,
        'Borracha', 2.00,
        'Caderno', 15.00,
        'Estojo', 25.00,
        'Transferidor', 4.20,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livro', 34.90)
print (prod)
print('-'*40)
print('{:^40}'.format('LISTA DE PREÇO'))
print('-'*40)
for pos in range(0, len(prod)):
        if pos % 2 == 0:
                print(f'{prod[pos]:.<30}',end='')
        else:
                print(f'R$ {prod[pos]:>6.2f}')
print('-'*40)
print("FIM")
