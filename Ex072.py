print('\033[1;51m Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.\n Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.\033[m')
contagem = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
cont = 'S'
while cont == 'S':
    n = int(input('Digite um Valor entre 0 e 20: '))
    while n < 0 or n >20:
        n = int(input('NÚMERO INVÁLIDO\nDigite um Valor entre 0 e 20:'))
    print(f'Você digitou o número {contagem[n]}')
    cont = str(input('Deseja Continuar? S / N : ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Opção Inválida\nDeseja Continuar? S / N : ')).strip().upper()[0]


