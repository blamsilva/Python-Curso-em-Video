nome = input(str('MARIA ALICE COSTA MARQUES DA SILVA:\n')).strip().upper()
while not nome == 'MARIA ALICE COSTA MARQUES DA SILVA':
    print('ERROU!, Tente Novamente.')
    nome = input(str('MARIA ALICE COSTA MARQUES DA SILVA:\n')).strip().upper()
print(f'PARABÉNS!!!!!!!!!!!!!!!!!!!!!\nVocê digitou corretamente.')