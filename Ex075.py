print("\033[1;51m Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:\n A) Quantas vezes apareceu o valor 9.\n B) Em que posição foi digitado o primeiro valor 3.\n C) Quais foram os números pares.\033[m")
lista = (int(input('Digite um valor:')),
         int(input('Digite outro valor:')),
         int(input('Digite mais outro valor:')),
         int(input('Digite um ultimo valor:')) )
print (lista)
print(f'O número 9 apareceu {lista.count(9)} vezes.')
if 3 in lista:
    print(f'O primeiro número 3 apareceu na posição {lista.index(3)}')
else:
    print('Não Apareceu o número 3 na tupla')
print('Números pares:', end=' ')
for l in lista:
       if l % 2 == 0:
         print(f'-> {l}', end=' ')