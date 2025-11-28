from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(FormaGeometrica):
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def calcular_perimetro(self):
        return self.l1 + self.l2 + self.l3

    def calcular_area(self):
        p = self.calcular_perimetro()
        s = p / 2
        return (s * (s - self.l1) * (s - self.l2) * (s - self.l3)) ** 0.5


# POLIMORFISMO 

formas = [
    Retangulo(5, 3),
    Triangulo(3, 4, 5),
]

for forma in formas:
    print("Forma:", forma.__class__.__name__)
    print("Área:", forma.calcular_area())
    print("Perímetro:", forma.calcular_perimetro())
    print("-" * 30)
# a lista formas contém objetos diferentes, mas o mesmo método é chamado: calcular_area e calcular_perimetro.