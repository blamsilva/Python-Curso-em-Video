print('\033[1:51m Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros '
      '\n opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, '
      '\n mesmo que algum dado não tenha sido informado corretamente. \033[m')
def ficha(nome='<Desconhecido>', gols=0):
    print(f'O Jogador {nome} fez {gols} gol(s) no campeonato.')
    nome = str(input('Nome do Jogador: '))
    gols = str(input('Número de Gols: '))
    if gols.isnumeric():
        g = int(gols)
    else:
        g = 0
    if nome.strip() == '':
        ficha(gols=gols)
    else:
        ficha(nome, gols)


# Programa Principal
ficha()
