print('\033[1;51m Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,\n peça a digitação novamente até ter um valor correto.\033[m')
sexo = str(input('Informe seu sexo F/M:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite uma opção válida,informe seu sexo F/M:')).strip().upper()[0]
print('Sexo {}, resgistrado com sucesso.'.format(sexo))
print('FIM')