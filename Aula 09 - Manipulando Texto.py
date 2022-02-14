frase = 'Curso em video Python'
print(frase.replace('Python','Android'))
'''Substitui a palavra Python pela Palavra Android'''
print (frase.upper())
'''O método .upper() transforma toda frase em maiúsculo'''
print(frase.lower())
'''O método .lower() transforma toda frase em minúsculo'''
print(frase.capitalize())
'''o metodo .capitalize() joga Todos os caracteres para minusculo e só o primeiro caracter vai ficar maiusculo'''
print(frase.title())
'''O método .title() busca todas as palavras e deixa apenas a primeira letra maiuscula'''
frase2 = '   Aprenda Python  '
print(frase2.strip())
'''o método .strip() remove os espaços desnecessários da frase'''
print(frase2.rstrip())
'''o método .rstrip() remove somente os espaços da direita'''
print(frase2.lstrip())
'''o método .rstrip() remove somente os espaços da esquerda'''
print(frase.split())
'''o método .split() faz uma divisao dentro da streame e divide entre espaços vazios cada palavra é colocada em uma lista nova'''
print('-'.join(frase))
'''O método .join() separa todas os caracteres com o caracter determinado '''

