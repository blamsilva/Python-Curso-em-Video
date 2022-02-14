print('\033[1;51m Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.\n O programa encerrará quando ele disser que quer mostrar 0 termos.\033[m ')
print('GERADOR DE PA')
print('=-='*10)
p = int(input('Primeiro termo:'))
r = int(input('Razão:'))
z = 10
soma = z
while z != 0:
    print(p,end='')
    print('->', end='')
    p += r
    z -= 1
    if z == 0:
        r = int(input('\nVocê quer mostrar mais quantos termos: \n0 - para Finalizar\nx - termos:'))
        if r > 0:
            z = r + z
            print(p, end='')
            print('->', end='')
            p += r
            z -= 1
            soma += r
print('Progressão Finalizada com {} termos mostrados.'.format(soma))
print('FIM')