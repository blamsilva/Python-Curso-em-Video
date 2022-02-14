class Error(Exception):
    pass
class InputErro(Error):
    def __init__(self, message):
        self.message = message
while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        if x > 10:
            raise InputErro('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputErro('Nota não pode ser menor que 0')
        print(x)
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputErro as ex:
        print(ex)
