print("\033[1;51m Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,\n mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.\033[m ")
from random import randint
print("===="*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print("===="*20)
npc = nus = cont = 0
tot = sit = 'P'
while sit == tot:
    npc = randint (0,10)
    nus = (int(input('Digite um valor:')))
    print("====" * 20)
    sit = str(input('Par ou Ímpar:\nP / I :')).strip().upper()
    while sit not in 'IP':
        sit = str(input('Opção inválida escolha:\nP / I:')).strip().upper()
    print("====" * 20)
    tot = (npc+nus)%2
    if tot == 0:
        tot = 'P'
    else:
        tot = 'I'
    if tot == sit:
        print("Você Acertou!")
        cont += 1
    print(f'Você disse: ({sit}) / Deu: ({tot})\n {npc} + {nus} = {npc+nus}\nResto de {npc+nus} / 2 = {(npc + nus)%2}' )
    print("====" * 20)
print(f'Você errou depois de {cont} acertos consecutivos.')
