#Parâmetros Opcionais
def somar(a=0, b=0, c=0): #Quando faço parametro=0 o Parametro pode receber nenhuma informação e recebe 0
    """
    -> Faz a soma de três velores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s=a+b+c
    print(f'A soma vale {s}')

# Programa Principal
somar(3,2,5)
somar(8,4)
