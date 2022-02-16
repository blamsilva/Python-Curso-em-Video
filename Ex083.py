print('\033[1;51m Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.'
      '\n Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. \033[m')

expr = str(input('Digite a expressão: '))
abrindo = 0
fechando = 0
for simbolo in expr:
    print(simbolo)
    if simbolo == '(':
        abrindo = abrindo + 1
        print(abrindo)
    elif simbolo == ')':
        fechando = fechando + 1
        print(fechando)

print(abrindo, fechando)
if abrindo == fechando:
    print('a expressão está correta!')
else:
    print('a expressão está errada!')

