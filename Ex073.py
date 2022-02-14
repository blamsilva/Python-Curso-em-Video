print("\033[1;51m Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,\n na ordem de colocação. Depois mostre:\n a) Os 5 primeiros times.\n b) Os últimos 4 colocados.\n c) Times em ordem alfabética.\n d) Em que posição está o time da Chapecoense.\033[m")
tabelab = 'Chapecoense', 'America-MG', 'Juventude', 'Cuiabá', 'CSA', 'Sampaio Corrêa', 'Ponte Preta', 'Operário', 'Avaí', 'CRB', 'Cruzeiro', 'Brasil de Pelotas', 'Guarani', 'Ec Vitória', 'Confiança', 'Náutico', 'Figuerense', 'Paraná', 'Botafogo SP', 'Oeste'
print('LISTA DE TIMES:')
for t in tabelab:
    print(t)
print('\nA) Os 5 primeiros colocados:')
print (tabelab[0:5])
print('\nb) Os últimos 4 colocados:')
print(tabelab[16:21])
print('\nc) Times em ordem alfabética:')
for a in sorted(tabelab):
    print(a)
print('\nd) Em que posição está o time da Chapecoense:')
print('{}º'.format((tabelab.index('Chapecoense')+1)))