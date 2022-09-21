def leiadinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \"{(entrada).upper()}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)
