print("\033[1;51mExercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nSeu programa deverá realizar a operação solicitada em cada caso.\033[m")
n1 = float(input('Digite um valor:'))
n2 = float(input('Digite outro valor:'))
opção = 0
while opção != 5:
    opção = int(input("Escolha a operação a ser realizada:\n1 - somar\n2 - multiplicar\n3 - maior\n4 - novos números\n5 - sair do programa\n:"))
    if opção == 1:
        print('A Soma de {} + {} = {}'.format(n1, n2, n1+n2))
    elif opção == 2:
        print('A Multiplicação de {} X {} = {}'.format(n1, n2, n1*n2))
    elif opção == 3:
        if n1 > n2:
            print('O Número {} é o maior digitado.'.format(n1))
        else:
            print('O Número {} é o maior digitado'.format(n2))
    elif opção == 4:
        n1 = float(input('Digite um novo valor:'))
        n2 = float(input('Digite outro novo valor:'))
print('FIM')
