
class Rectangulo:
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2*(self.base + self.altura)


rectangulo = Rectangulo(5,3)

print(rectangulo.area()) #Esto muestra el area
print(rectangulo.perimetro()) ##Esto muestra el perimetro