print("Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. ")

r = float(input("Digite o valor em R$:"))
d = float(input("Digite a cotação do Dolar:"))
c = r/d
print("Com R${} e o Dolar custando ${} ,Você consegue comprar {:.2f} Dolares".format(r, d, c))