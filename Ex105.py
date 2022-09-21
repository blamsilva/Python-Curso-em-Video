print('\033[1:51m Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas'
      'de alunos \n e vai retornar um dicionário com as seguintes informações: \n – Quantidade de notas '
      '\n – A maior nota \n – A menor nota \n – A média da turma \n – A situação (opcional) \033[m')
def notas(*n, sit=False):
    '''
    -> Funcao para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma;
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] > 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'RUIM'

    return r


# Programa Pricipal
resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)