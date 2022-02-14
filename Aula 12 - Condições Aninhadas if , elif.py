'''Nessa aula, vamos aprender como criar estruturas condicionais aninhadas,
 usando os comandos if.. elif.. else em programas Python.'''
nome = str(input('Qual é o seu nome:')).strip().capitalize()
if nome == 'Bruno':
    print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('{}, seu nome é bem popular no Brasil.'.format(nome))
elif nome in 'Ana Cláudia Juliana Michelle Alice Júlia':
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}.'.format(nome))