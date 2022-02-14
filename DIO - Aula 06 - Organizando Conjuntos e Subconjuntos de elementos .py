conjunto = {1, 2, 3, 4, 4, 2}
print(conjunto) #elementos duplicados não são impressos repetidos
conjunto.add(5) #.add adiciona elemento ao conjunto
conjunto.discard(4) #.discard elimina elemento do conjunto
print(conjunto)
print('=-'*20)
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
print(f'Conjunto 1 = {conjunto}')
print(f'Conjunto 2 = {conjunto2}')
print('=-'*20)
conjunto_uniao = conjunto.union(conjunto2) #.union() faz a uniao entre dois conjuntos
print('União 1 e 2')
print(conjunto_uniao)
print('=-'*20)
print('Interseccao 1 e 2')
conjunto_interseccao  = conjunto.intersection(conjunto2) #busca o item de interseccao nos dois conjuntos
print(conjunto_interseccao)
print('=-'*20)
print('Diferença entre 1 e 2')
conjunto_diferença = conjunto.difference(conjunto2) #busca os elementos que só tem no conjunto 1
print(conjunto_diferença)
conjunto_diferença2 = conjunto2.difference(conjunto) #busca os elementos que só tem no conjunto 2
print('Diferença entre 2 e 1')
print(conjunto_diferença2)
print('=-'*20)
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2) # imprime só os elementos que não tem nos dois conjutos.
print(f'Diferença simetrica: {conjunto_diff_simetrica}')
print('=-'*20)
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
print(f'Conjunto A = {conjunto_a}')
print(f'Conjunto B = {conjunto_b}')
conjunto_subset = conjunto_a.issubset(conjunto_b) # verifica por TRUE or FALSE se o conjunto a e subconjunto do conjunto b
print('A é subconjunto de B ? ')
print(conjunto_subset)
print('=-'*20)
conjunto_subset = conjunto_b.issuperset(conjunto_a) # Verifica por True or False se o conjunto é um superconjunto de outro conjunto
print('B é um superconjunto de A?')
print(conjunto_subset)
print('=-'*20)
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(f'A Lista dos animais é : {lista}')
conjunto_animal =  set(lista) #transforma a lista em conjunto
print('O conjunto de animais é:')
print(conjunto_animal)
print('=-'*20)
lista_animais = list(conjunto_animal) #converte o conjunto para lista
print('A lista de Animais sem repetidos ficou:')
print(lista_animais)