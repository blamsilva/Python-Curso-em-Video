# dados=dict() Declara um dicionário
# dados={} Declara um dicionário
dados = {'nome': 'Pedro', 'idade': 25} # Declara um dicionário com dados já incluso
print(dados['nome'])
print(dados['idade'])
dados['sexo']='M' # acrescenta um novo elemento
del dados['idade'] # del remove um elemento
filme={'titulo':'Star Wars',
       'ano':1977,
        'diretor':'George Lucas'
            }
print(filme.values()) # imprime só os dados
print(filme.keys()) # imprime só as chaves
print(filme.items()) # imprime todos os valores e chaves
for k, v in filme.items(): #Exemplo de Estrutura de repetição no dicionário
    print(f'O {k} é {v}') 


