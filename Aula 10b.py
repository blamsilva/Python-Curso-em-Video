nome = str(input('Digite Seu Nome:')).upper()
if nome == 'RENATA':
    print('QUE NOME FEIO, TROQUE DE NOME')
elif nome == 'BRUNO':
        print('QUE NOME BONITO.')
else:
    print('Seu nome é normalzinho.')
print('FIM')
print("*"*50)
n1 = float(input('Digite a Primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa Parabéns.')
else:
    print('Sua média foi ruim, Estude mais.')
