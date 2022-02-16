lanche = ['Hamburguer' , 'Suco', 'Pizza', 'Pudin']  #As Listas utilizam conchetes []
#Listas São mutáveis
lanche[3] = 'Picolé'
print(lanche)
#adicinando itens a lista
lanche.append('Pudin')
print(lanche)
#adicionando item em uma determinada posição
lanche.insert(0,'cachorro Quente')
print(lanche)
#Para eliminar itens podem ser usados 3 comandos o del, pop, remove:
del lanche[3]
print(lanche)
lanche.pop(3) #se estiver vazio remove o ultimo elemento.
print(lanche)
lanche.remove('Pudin')
print(lanche)
if 'Suco' in lanche:
    lanche.remove('Suco')
print(lanche)
print('----'*10)
valores = list(range(4,11))
valores.sort() #sort coloca os itens em ordem crescente
# sort(reverse=True) coloca os valores em ordem inversa
print(len(valores))
print(valores)
print('----'*10)
for c, v in enumerate(valores): #enumerate() faz o programa dizer o item e a posição do item na lista.
    print((f'Na posição {c} encontrei o valor {v}!'))
print('Cheguei ao final da lista')
print('----'*10)
b = a[:] # Isso faz uma cópia de uma lista sem ter ligação entre si.