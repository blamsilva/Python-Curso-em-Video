# Interactive Help
# help()
# print(input.__doc__)
# Docstrings

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :parametro i: início da contagem
    :parametro f: fim da contagem
    :parametro p: passo da contagem
    :return: sem retorno
    """

    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


# Programa Principal
contador(2, 10, 2)

help(contador)

