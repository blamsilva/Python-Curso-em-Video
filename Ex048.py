print('\033[1;51mExercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três\ne que se encontram no intervalo de 1 até 500.\033[m')
s = 0
v = 0
for n in range(1, 500, 2):
    if n % 3 == 0:
        v += 1
        s += n
        print(n, end=' ')
print('\nTEMOS {} números ímpares multiplos de 3 no intervalo entre 1 e 500'.format(v))
print('A Soma de todos eles é {}\n'.format(s))
print('FIM')
