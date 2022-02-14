print('''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.''')
nome = str(input('Digite o seu nome Completo:')).strip()
print(nome.upper())
print(nome.lower())
snome = nome.replace(' ', '')
'''o método .replace foi utilizado para substituir os epaços em branco o retirando'''
print('Seu nome completo possui {} letras.'.format(len(snome)))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
'''Outra Forma de fazer a contagem das letras utilizando a contagem de espaços utilizados diminuindo da quantidade de espaços em branco'''
listanome = nome.split()
print('Seu primeiro nome é {} e possui {} letras.'.format(listanome[0],len(listanome[0])))
