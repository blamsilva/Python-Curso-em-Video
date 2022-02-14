print('Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,\nse ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.\n Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.')
from datetime import date
nasc = int(input('Digite o ano de seu nascimento:'))
atual = date.today().year
print(nasc, atual)
if atual - nasc == 18:
    print('Você precisa se alistar agora.')
elif atual - nasc > 18:
    print('Você deviria ter se alistado há {} anos,Compareca a um quartel e Regularize.'.format(atual-(nasc+18)))
elif atual - nasc < 18:
    print('Você precisa se alistar daqui há {} anos.'.format(18-(atual-nasc)))