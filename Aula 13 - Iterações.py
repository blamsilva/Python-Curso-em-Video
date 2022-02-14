from time import  sleep
print('Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender.')
print('==='*20)
print('\033[1mEXEMPLO - 1:\033[m')
for c in range(0, 4):
    print(c)
print('Acabou')
print('==='*20)
print('\033[1mEXEMPLO - 2:\033[m')
for c in range(0, 6):
    print ('Oi')
print('Fim')
print('==='*20)
print('\033[1mEXEMPLO - 3:\033[m')
for c in range(10,0,-1):
    print(c)
    sleep(.1)
print('Fim')
print('==='*20)
print('\033[1mEXEMPLO - 4:\033[m')
n = int(input('Digite um número:'))
for c in range(0, n+1):
    print (c)
print('FIM')
print('==='*20)
print('\033[1mEXEMPLO - 5:\033[m')
i=int(input('INICIO:'))
f=int(input('FIM:'))
p=int(input('PASSO:'))
for c in range(i, f+1, p):
    print(c)
print('FIM')
print('==='*20)
print('\033[1mEXEMPLO - 6:\033[m')
for c in range(0,3):
    n = int(input('Digite um Número:'))
print('FIM')
print('==='*20)
print('\033[1mEXEMPLO - 7:\033[m')
s = 0
for c in range(0,3):
    n = int(input('Digite um Número:'))
    s = s + n
print(s)
print('FIM')
print('==='*20)
