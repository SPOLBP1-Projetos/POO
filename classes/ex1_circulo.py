import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio**2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

    def calcular_diametro(self):
        return 2 * self.raio


circ1 = Circulo(5)

print(f"O raio desta figura é: {circ1.raio}.")
print(f"A área é: {circ1.calcular_area():.3f}")
print(f"O perímetro é: {circ1.calcular_perimetro():.3f}")
print(f"O diâmetro é: {circ1.calcular_diametro()}")