class Calculadora:
    def __init__(self, num1, num2):
        self.a =  num1
        self.b = num2

    def soma (self): # define as variáveis de um método
        return self.a + self.b # define o retorno da operaçao com as variáveis

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b
calculadora = Calculadora(10, 2)
print(calculadora.a)
print(calculadora.b)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())


