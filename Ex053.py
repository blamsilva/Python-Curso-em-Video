print('\033[1;51m Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:\n APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.\033[m')
frase = str(input('Digite uma frase e verefique se ela é um palíndromo:\n')).upper().replace(' ','')
inverso=''
for letra in range(len(frase) -1, -1, -1):
    inverso += frase[letra]
if frase == inverso:
    print('A Frase Digitada é um palídromo.')
else:
    print('A Frase Digitada não é um palídromo')
print('===='*20)
print('\033[1mOUTRA MANEIRA DE FAZER SEM UTILIZAr O for E UTILIZANDO fatiamento.\033[M')
frase = str(input('Digite uma frase e verefique se ela é um palíndromo:\n')).upper().replace(' ','')
inverso = frase[::-1]
if frase == inverso:
    print('A Frase Digitada é um palídromo.')
else:
    print('A Frase Digitada não é um palídromo')
    