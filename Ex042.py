print('Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:\n– EQUILÁTERO: todos os lados iguais\n– ISÓSCELES: dois lados iguais, um diferente\n– ESCALENO: todos os lados diferentes ')
l1 = float(input('Digite um lado:'))
l2 = float(input('Digite outro lado:'))
l3 = float(input('Digite outro lado:'))
if l1 == l2 == l3:
    tipo = 'EQUILÁTERO'
elif l1 == l2 and l1 != l3 or l2 == l3 and l2 != l1 or l3 == l1 and l3 != l2:
    tipo='ISÓCELES'
else:
    tipo ='ESCALENO'
print(tipo)
if l1 < (l2+l3) and l2 < (l1+l3) and l3 < (l1+l2):
    print('As medidas \033[1;34m{:.2F}\033[m, \033[1;35m{:.2F}\033[m e \033[1;36m{:.2F}\033[m podem formar um triângulo do tipo {}'.format(l1, l2, l3, tipo))
else:
    print('As medidas \033[1;34m{:.2F}\033[m, \033[1;35m{:.2F}\033[m e \033[1;36m{:.2F}\033[m \033[1;31mNÃO PODEM FORMAR UM TRIÂNGULO\033[m'.format(l1, l2, l3))
