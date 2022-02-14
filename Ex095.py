print('\033[1;51m Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,'
      '\n incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador  \033[m')
print('\033[1:51m Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. \n O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. \n No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.\033[m')
time = list()
tabela = dict()
tabela['nome'] = str(input('Nome do Jogador: '))
tabela['partidas'] = int(input(f'Quantas partidas {tabela["nome"]} jogou? '))
gols = []
totg = 0
for c in range(1, tabela["partidas"]+1):
    golp = int(input(f'Quantos gols na partida {c}? '))
    gols.append(golp)
    totg += golp
tabela['gol'] = gols
tabela['total'] = totg
print('-=-='*20)
print(tabela)
print('-=-='*20)
for f, l in tabela.items():
    print(f'- O Campo {f} tem o valor {l}')
print('-=-='*20)
print(f'O Jogador {tabela["nome"]} jogou {tabela["partidas"]} partidas')
for c in range(1, tabela["partidas"]+1):
    print(f'    => Na Partida {c}, fez {gols[c-1]} gols')
print(f'Foi um total de {tabela["total"]} gols')