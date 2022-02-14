print('\033[1;51m Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.\n No final, mostre o conteúdo da estrutura na tela.\033[m')
sit = {}
while True:
    sit['nome'] = str(input(('Nome: '))).strip().capitalize()
    sit['media'] = float(input('Digite sua média: '))
    if sit['media'] > 6.99:
            sit['situacao'] = 'APROVADO'
    else:
            sit['situacao'] = 'REPROVADO'
    break
print('-='*50)
print(f'- o nome é igual a {sit["nome"]}')
print(f'- média é igual a {sit["media"]}')
print(f'- situação é igual a {sit["situacao"]}')
