print("\033[1;51m Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.\n No final,"
      "mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.\033[m")

a = []
cont = 0
maior = 0
menor = 0
while cont <= 4:
    a.append(int(input(f"Digite um valor na posição {cont}: ")))
    if cont == 0:
        maior = menor = a[cont]
    else:
        if a[cont] > maior:
            maior = a[cont]
        if a[cont] < menor:
            menor = a[cont]
    cont = cont + 1
print("------"*10)
print(f'Você digitou os valores {a}')
print(f'O maior valor digitado foi {maior} na posições ', end='')
for i, v in enumerate(a):
    if v == maior:
        print(f' {i}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posições ', end='')
for i, v in enumerate(a):
    if v == menor:
        print(f' {i}...', end='')
print()