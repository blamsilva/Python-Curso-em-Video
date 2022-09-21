from utilidadescev import moeda

print('\033[1:51m Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados '
      '\n moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote '
      '\n e mantenha tudo funcionando. \033[m')


p = float(input('\nDigite o preço: R$'))
moeda.resumo(p)
