print('\033[1:51m Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),'
      '\n diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções. \033[m')

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(p, 10)}')

