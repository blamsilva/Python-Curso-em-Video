print('Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,\n'
      ' em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.')
frase = str(input('Digite uma frase:')).lower()
print('Analisando a Frase')
n = frase.count('a') + frase.count('à') + frase.count('á')
print('Aparecem {} "a" na frase.'.format(n))
print('A Primeira Letra "A" apace na posição {}'.format(frase.find('A')+1))
print('A última letra "A aparece na posição {}'.format(frase.rfind('A')+1))