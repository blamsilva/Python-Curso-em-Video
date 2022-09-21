import moeda

print('\033[1:51m Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, '
      '\n uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções '
      '\n que já temos no módulo criado até aqui. \033[m')


p = float(input('\nDigite o preço: R$'))
moeda.resumo(p)
