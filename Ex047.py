print('\033[1;51mExercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.\033[m')
for c in range(1,51 ,):
    if c % 2 == 0:
        print(c, end=' ')
print('\nFIM')
print('==='*20)
print('SOLUÇÃO 2:')
for n in range(2, 51, 2):
    print(n, end=' ')
print('\nFIM')