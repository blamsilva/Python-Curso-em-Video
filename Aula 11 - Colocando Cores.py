'''Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar
cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.'''
'''\033[Stylo;cor texto;cor do fundo m'''
print('\033[4;36;41mA Casa é Amarela\033[m')
'''Stylo
0 - sem Stylo
1 - Negrito
4 - Sublinhado 
7 - Inverte as configurações'''

'''Cor Texto
30 - Branco
31 - Vermelho
32 - Verde
33 - Amarelo
34 - Azul
35 - Lilas
36 - Azul Claro
37 - Cinza'''

print('\033[0;30;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;30mTeste\033[m')
