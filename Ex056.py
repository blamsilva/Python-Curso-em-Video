print('\033[1;51m Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,\n mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.\033[m')
sexof20 = 0
idadev = 0
nomev = ''
somaidade = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da {}º pessoa:'.format(c))).capitalize().strip()
    idade = int(input('Digite a idade da {}º pessoa:'.format(c)))
    sexo = str(input('Digite Sexo:\n{F} - Feminino\n{M} - Masculino\n:')).upper().strip()
    somaidade += idade
    if sexo == 'F' and idade < 20:
        sexof20 += 1
    if sexo == 'M' and idade > idadev:
        idadev = idade
        nomev = nome
media = somaidade/4
print('A média de idade do grupo é {}\nO nome do Homem mais velho é {} e tem {} anos de idade\nExistem {} mulheres menores de 20 anos.'.format(media, nomev, idadev,sexof20))

