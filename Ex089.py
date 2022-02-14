print('\033[1;51m Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.\n No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.\033[m')
contador = 0
nota = list ()
boletim = list()
while True:
    print("=" * 50)
    nota.append(str(input('Digite seu nome: ')))
    nota.append(float(input('Digite a 1ª nota:')))
    nota.append(float(input('Digite a 2ª nota:')))
    nota.append((nota[1]+nota[2])/2)
    boletim.append(nota[:])
    nota.clear()
    cont = str(input("Quer Continuar S/N :")).strip()[0]
    contador += 1
    if cont not in "Ss":
        break
print("="*50)
print(f'{"Nº":^5}{"NOME":^10}{"Média":^10}')
print("-"*25)
for c in range(0, contador):
    print(f'{c:<5}{boletim[c][0]:<10}{boletim[c][3]:^10}')
print("-"*25)
while True:
    cont = int(input('Mostrar Nota de qual aluno?  999 - Sair / Nº :'))
    if cont == 999:
        break
    if cont <= contador-1:
        print(f'As Notas de {boletim[cont][0]} são Nota 1 = {boletim[cont][1]} ; Nota 2 = {boletim[cont][2]}')
        print("-"*25)
    else:
        cont = int(input('( Nº INVÁLIDO )\nMostrar Nota de qual aluno?  999 - Sair / Nº :'))
print('FIM')
