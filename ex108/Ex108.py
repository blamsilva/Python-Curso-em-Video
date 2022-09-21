import moeda
print('\033[1:51m Exercício Python 108: Adapte o código do desafio #107, '
      '\n criando uma função adicional chamada moeda que consiga '
      '\n mostrar os números como um valor monetário formatado. \033[m')



p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(p, 10))}')