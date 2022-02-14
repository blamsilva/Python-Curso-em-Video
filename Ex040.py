print('Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, \nmostrando uma mensagem no final, de acordo com a média atingida:\n– Média abaixo de 5.0: REPROVADO\n– Média entre 5.0 e 6.9: RECUPERAÇÃO\n– Média 7.0 ou superior: APROVADO')
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
média = (nota1+nota2)/2
if média < 5:
    print('Sua média foi {:.2f} e você foi \033[1;31mREPROVADO\033[M'.format(média))
elif média >= 5 and média < 7:
    print('Sua média foi {:.2f} e você está de \033[1;34mRECUPERAÇÃO\033[m'.format(média))
elif média > 6.9 and média < 10.01:
    print('Sua média foi {:.2f} e você está \033[1;32mAPROVADO\033[m'.format(média))


