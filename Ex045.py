print('Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.')
from random import randint
from time import sleep
print('[1] - Pedra\n[2] - Papel\n[3] - Tesoura')
esc = int(input('Escolha:'))
pc = randint(1,3)
print('===='*20)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('===='*20)
sleep(2)
if esc ==1:
    esc = 'Pedra'
elif esc ==2:
    esc = 'Papel'
elif esc == 3:
    esc = 'Tesoura'
else:
    print('Você Escolheu uma opção inválida')
if pc == 1:
    pc = 'Pedra'
elif pc == 2:
    pc = 'Papel'
elif pc == 3:
    pc = 'Tesoura'
print('Você escolheu ({})\nO PC escolheu ({})'.format(esc, pc))
print('===='*20)
if esc == pc:
    print ('DEU EMPATE')
elif esc == 'Tesoura' and pc == 'PAPEL' or esc == 'Pedra' and pc == 'Tesoura' or esc == 'Papel' and pc == 'Pedra':
    print('O JOGADOR VENCEU')
else:
    print('O PC VENCEU')
