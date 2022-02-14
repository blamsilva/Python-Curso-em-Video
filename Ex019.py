import random
print('Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa \nque ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.')
a1 = input('1º Aluno:')
a2 = input('2º Aluno:')
a3 = input('3º Aluno:')
a4 = input('4º Aluno:')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido para apagar o quadro foi {}.'.format(escolhido))
