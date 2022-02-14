print('Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.')
nome = str(input('Digite seu nome completo:')).upper().strip()
print('O seu nome tem SILVA: {}'.format('SILVA'in nome))
