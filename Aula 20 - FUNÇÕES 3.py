def contador(*núm):
  print(núm)

# PROGRAMA PRINCIPAL 1
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print('-*-'*30)

def contador2(*núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')


# PROGRAMA PRINCIPAL 2
contador2(2, 1, 7)
contador2(8, 0)
contador2(4, 4, 7, 6, 2)

print('-*-'*30)

def contador3(*núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')

# PROGRAMA PRINCIPAL 3
contador3(2, 1, 7)
contador3(8, 0)
contador3(4, 4, 7, 6, 2)