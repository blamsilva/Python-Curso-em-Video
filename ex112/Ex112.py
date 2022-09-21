from utilidadescev import moeda
from utilidadescev import dado

print('\033[1:51m Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo '
      '\n chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), '
      '\n mas com uma validação de dados para aceitar apenas valores que seja monetários. \033[m')


p = dado.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
