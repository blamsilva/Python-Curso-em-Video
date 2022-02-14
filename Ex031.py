print('Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.\n Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.')
viagem = float(input('Digite a distância da viagem em km:'))
if viagem <= 200:
    custo = (viagem*0.50)
    print('Uma Viagem de {}km custará R${:.2f}'.format(viagem, custo))
else:
    custo = (viagem*0.45)
    print('Uma Viagem de {}km custará R${:.2f}'.format(viagem, custo))
print('FIM')
