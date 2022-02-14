print('\033[1;51m Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,\n mostrando os 10 primeiros termos da progressão usando a estrutura while.\033[m')
print('GERADOR DE PA')
print('=-='*10)
p = int(input('Primeiro termo:'))
r = int(input('Razão:'))
z = 10
while not z == 0:
    print(p,end='')
    print('->', end='')
    p += r
    z -= 1
print('FIM')