print('Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer\n e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.')
n = int(input('Digite um valor inteiro:'))
print('Escolha uma opção a seguir para converter o número:')
e = int(input('1 - Binário\n2 - Octal\n3 - Hexadecimal\n4 - TODAS ANTERIORES\nESCOLHA: '))
b = bin(n)
o = oct(n)
h = hex(n)
if e == 1:
    print('O número {} convertido para base Binária fica {}'.format(n, b[2:]))
elif e == 2:
    print('O número {} convertido para base octal fica {}'.format(n, o[2:]))
elif e == 3:
    print('O número {} convertido para base hexadecimal fica {}'.format(n, h[2:]))
elif e == 4:
    print('O número {} convertido para base Binária fica ({})'.format(n, b[2:]))
    print('O número {} convertido para base octal fica ({})'.format(n, o[2:]))
    print('O número {} convertido para base hexadecimal fica ({})'.format(n, h[2:]))
else:
    print('VOCÊ DIGITOU A OPÇÃO ERRADA')
