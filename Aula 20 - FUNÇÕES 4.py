valores = [7,2,5,0,4]
print(valores)

print('-*'*30)
print('Exemplo 2')
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
