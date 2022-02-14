print("\033[1;51m Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.\n A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:\n A) quantas pessoas tem mais de 18 anos.\n B) quantos homens foram cadastrados.\n C) quantas mulheres tem menos de 20 anos.\033[m ")
maiorida = cadh = mul = 0
while True:
    idade = int(input('Digite sua Idade:'))
    sexo = str(input('Digite Seu Sexo:\nF - Feminino\nM - Masculino\n: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('OPÇÃO INVÁLIDA\nDigite Seu Sexo:\nF - Feminino\nM - Masculino\n: ')).strip().upper()[0]
    if idade > 18:
        maiorida += 1
    if sexo == 'M':
        cadh += 1
    if sexo == 'F':
        if idade < 20:
            mul += 1
    cont = str(input('Deseja Continuar S / N:')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('OPÇÃO INVÁLIDA\nDeseja Continuar S / N:')).strip().upper()[0]
    print("====" * 20)
    if cont == 'N':
        break
print(f'\033[1;51m A) ({maiorida}) Maiores de 18 anos \n B) ({cadh}) Homens Cadastrados \n C) ({mul}) Mulheres menores de 20 anos \033[m')
