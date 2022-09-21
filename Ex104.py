print('\033[1:51m Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma '
      '\n semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. '
      '\n Ex: n = leiaInt(‘Digite um n: ‘) \033[m')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m.')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você ababou de digitar o número {n}')