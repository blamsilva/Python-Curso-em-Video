print('\033[1:51mExercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:\n1 – à vista dinheiro/cheque: 10% de desconto\n2 – à vista no cartão: 5% de desconto\n3 – em até 2x no cartão: preço formal\n4 – 3x ou mais no cartão: 20% de juros\033[m')
preço = float(input('Digite o valor do produto: R$ '))
pgmt = int(input('Escolha a forma de pagamento:'))
if pgmt == 1:
    total = preço*0.9
    print('O Produto de Valor R${:.2f} teve um desconto de 10% e ficou R${:.2f}'.format(preço, total))
elif pgmt == 2:
    total = preço*0.95
    print('O Produto de Valor R${:.2f} teve um desconto de 5% e ficou R${:.2f}'.format(preço, total))
elif pgmt == 3:
    total = preço
    print('O Produto de Valor R${:.2f} não teve um desconto ficou R${:.2f} em 2x de R${:.2f}'.format(preço, total, total/2))
elif pgmt == 4:
    total = preço * 1.2
    parc = int(input('Quantas Parcelas:'))
    tparc = total/parc
    print('O Produto de Valor R${:.2f} teve um acrescimo de 20% e ficou R${:.2f} parcelado em {}x de R${:.2f}'.format(preço, total, parc , tparc))
else:
    print('\033[1;30;41mVOCÊ ESCOLHEU UMA OPÇÃO INVÁLIDA.\033[m')
print('FIM')
