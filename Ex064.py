print("\033[1;51m Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.\n O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.\n No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).\033[m")
n = 0
cont = -1
soma = - 999
while n != 999:
    n = int(input('999 - FINALIZAR\nDIGITE UM VALOR:'))
    cont += 1
    soma += n
print('Foram digitados {} e o valor da soma é {}'.format(cont, soma))
print("FIM")