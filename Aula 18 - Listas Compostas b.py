teste= list()
teste.append('Bruno')
teste.append(31)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galera = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria',45]]
print(galera[2][0])
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
galera.clear()#apaga a lista galera
dado = list()
totmai = totmen = 0
dado.clear()
galera.clear()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(input('Idade: '))
    galera.append(dado[:])
    dado.clear()
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é m,menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
