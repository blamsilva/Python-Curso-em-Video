print('\033[1;51m Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos \n e '
      'cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.\n No final, serão exibidos '
      'todos os valores únicos digitados, em ordem crescente.\033[m')

lista = []
cont = "S"
while cont == 'S':
    novo = (int(input('Digite um valor: ')))
    if novo not in lista:
            lista.append(novo)
    cont = str(input('Deseja Continuar S / N : ')).strip().upper()
lista.sort()
print(lista)
