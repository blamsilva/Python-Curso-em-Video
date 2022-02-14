print('\033[1;51mExercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)\n e mostre seu status, de acordo com a tabela abaixo:\n– IMC abaixo de 18,5: Abaixo do Peso\n– Entre 18,5 e 25: Peso Ideal\n– 25 até 30: Sobrepeso\n– 30 até 40: Obesidade\n– Acima de 40: Obesidade Mórbida \033[m')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc =  peso/(altura**2)
if imc < 18.5:
    tipo = '\033[1;30mAbaixo do Peso\033[m'
elif imc >= 18.5 and imc < 25:
    tipo = '\033[1;34mPeso Ideal\033[m'
elif imc >= 25 and imc < 30:
    tipo = '\033[1;31;43mSobrepeso\033[m'
elif imc >= 30 and imc <= 40:
        tipo = '\033[1;31;43mObesidade\033[m'
else:
    tipo = '\033[1;30;41mObesidade Mórbida\033[m'
print('Com o Peso \033[1;31m{:.2f}\033[m Kg e Altura \033[1;32m{:.2f}\033[m Metros possui o imc de \033[1;33m{:.1f}\033[m do tipo : {}'.format(peso, altura, imc, tipo))