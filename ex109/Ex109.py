import moeda
print('\033[1:51m Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem '
      '\n um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),'
      '\n desenvolvida no desafio 108.\033[m')



p = float(input('\nDigite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p, True))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p, True))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10, True))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(p, 10, True))}')