print('\033[1;51mExercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.\033[m')
n = int(input('Digite um valor e veja sua Taboada:'))
i = 0

for c in range(1,11):
    print('{} X {:2} = {:3}'.format(n, c ,n*c))
    