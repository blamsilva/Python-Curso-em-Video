print('\033[1;51m Exercício Python 67: Faça um programa que mostre a tabuada de vários números,\n um de cada vez, para cada valor digitado pelo usuário.\n O programa será interrompido quando o número solicitado for negativo.\033[m')
tab = 1
while True:
    n = int(input('Digite um número e veja sua tabuada:'))
    if n < 0:
        break
    while tab < 11:
        print(f'{n} X {tab} = {n*tab}')
        tab += 1
    tab = 1
print('FIM')