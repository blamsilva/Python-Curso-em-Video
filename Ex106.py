from time import sleep
print('\033[1:51m Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. '
      '\n O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’,'
      '\n o programa se encerrará. Importante: use cores. \033[m')
c = ('\033[m', # 0 - Sem Cores
     '\033[0;30;41m', # 1 - Vermelho
     '\033[0;30;42m', # 2 - Verde
     '\033[0;30;43m', # 3 - Amarelo
     ' \033[0;30;44m',# 4 - Azul
     '\033[0;30;45m', # 5 - Roxo
     '\033[7;51m'     # 6 - Branco
    );

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!',1)
