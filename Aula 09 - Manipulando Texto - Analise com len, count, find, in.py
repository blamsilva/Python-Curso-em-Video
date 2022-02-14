frase = 'Curso em video Python'
print(len(frase))
'''a função len determina o comprimento da frase quantos espaços ela tem'''
print(frase.count('o'))
'''a função .count busca quanto caracteres determinado tem na frase e conta ele diferencia maiusculo do minusculo'''
print(frase.count('o',0,13))
'''Ele vai contar quantos 'o' com fatiamento da posição 0 até a posição 12'''
print(frase.find('deo'))
'''Ele procura os caracteres 'deo' e indica a posição que ele começou'''
print(frase.find('android'))
'''Quando não existe os caracteres na string ele retorna a posição -1'''
print('Curso' in frase)
'''Ele verifica se existe os caracteres determninado na frase retornando com verdadeiro ou falso, diferencia maiusculo e minusculo'''
