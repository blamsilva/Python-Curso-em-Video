print('Exercício Python 29: Escreva um programa que leia a velocidade de um carro.\nSe ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.')
v = int(input('Digite a velocidade do Carro em km/h:\n'))
if v > 80:
    m = (v-80)*7
    print('Sua velocidade foi de {}km/h você está {}km/h acima do permitido e a multa vai custar R${:.2f}'.format(v, v-80, m))
else:
    print('Continue andando sempre na velocidade da via, Parabéns.')
print('FIM')