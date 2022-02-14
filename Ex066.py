print("\033[1;51m Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.\n O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.\n No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).\033[m")
n = soma = cont = 0
while True:
    n = int(input('999 - PARA PARAR\nDigite um valor:'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} números e o total da soma foi de {soma}')
