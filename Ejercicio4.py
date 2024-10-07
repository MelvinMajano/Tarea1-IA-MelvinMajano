

class Calculadora:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def suma(self):
        return self.a +self.b
    def resta(self):
        return self.a-self.b
    def multiplicacion(self):
        return self.a*self.b
    def division(self):
        if self.b==0:
            return 'La division entre 0 es indefinida'
        else:
            return self.a/self.b

calculadora=Calculadora(4,8)
print(calculadora.suma())
print(calculadora.resta())
print(calculadora.multiplicacion())
print(calculadora.division())

calculadora2=Calculadora(5,0)
print(calculadora2.suma())
print(calculadora2.resta())
print(calculadora2.multiplicacion())
print(calculadora2.division())
