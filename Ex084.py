print('\033[1;51m Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:\n A) Quantas pessoas foram cadastradas.\n B) Uma listagem com as pessoas mais pesadas.\n C) Uma listagem com as pessoas mais leves.\033[m')
pessoas = list() # lista contendo pessoa e idade separados #
grupo = list() # Lista de pessoas e idades juntos em grupo #
maior = list() # Lista do nome da maior idade #
menor = list() # Lista do nome da menor idade #
cad = maiorpeso = menorpeso = 0 # variáveis #
cont = "S"
while cont in 'S': # condição ENQUANTO cont for 'S' faça. #
    print("=" * 40)
    pessoas.append(input('Digite seu nome:').capitalize()) # Digitar o nome #
    pessoas.append(int(input('Digite seu peso:'))) # Digitar o peso #
    cad += 1 # Soma mais 1 no Contador de cadastrados #
    grupo.append(pessoas[:]) # Adiciona a lista pessoas na lista grupo #
    if menorpeso == 0: # se menor peso for 0 faça #
        menorpeso = pessoas[1]
    if maiorpeso == 0: # se maior peso for 0 faça #
        maiorpeso = pessoas[1]
    if pessoas[1] > maiorpeso: # se o item[1] da lista pessoas for maior que maiorpeso faça #
        maior.clear() #apaga a lista maior #
        maiorpeso = pessoas[1]
        maior.append(pessoas[0]) # adiciona o item [0] da lista pessoas na lista maior #
    if pessoas[1] == maiorpeso: # se o item[1] da lista pessoas for igual que maiorpeso faça #
        maiorpeso = pessoas[1]
        maior.append(pessoas[0]) # adiciona o item [0] da lista pessoas na lista maior #
    if pessoas[1] < menorpeso: # se o item[1] da lista pessoas for menor que menorpeso faça #
        menor.clear() # apaga a lista menor
        menorpeso = pessoas[1]
        menor.append(pessoas[0]) # adiciona o item [0] da lista pessoas na lista menor
    if pessoas[1] == menorpeso: # se o item[1] da lista pessoas for igual que menorpeso faça #
        menorpeso = pessoas[1]
        menor.append(pessoas[0])# adiciona o item [0] da lista pessoas na lista menor
    cont = input('Deseja Continuar? S/N : ').strip().upper()[0] # input de Pergunta se quer continuar #
    if cont not in "SN": #Verifica se a resposta está dentro das opções S ou N e refaz até está dentro das opções #
        cont = input('Opção Inválida\nDeseja Continuar? S/N : ').strip().upper()[0]
    pessoas.clear() # apaga a lista pessoas #
print('='*40)
print(f'Você cadastrou {cad} pessoas')
print(f'O maior peso foi de {maiorpeso} Kg, Peso de {maior}')
print(f'O menor peso foi de {menorpeso} Kg, Peso de {menor}')
print('='*40)
