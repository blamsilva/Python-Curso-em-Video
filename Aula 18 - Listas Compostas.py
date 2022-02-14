# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.#
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
pessoas =list()
pessoas.append(dados[:])
print(pessoas)
pessoas=[['Pedro',25],['Maria',19],['João',32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
