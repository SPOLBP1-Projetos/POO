class Animal: # classe base
    def __init__(self, nome: str):
        self.nome = nome
    
    def emitir_som(self):
        return "som generico" 
class Cachorro(Animal): # classe filha
    def emitir_som(self):
        return "Au Au!"
    
    def latir(self):
        return "Woof woof!" 
class Gato(Animal): # classe filha
    def emitir_som(self):
        return "Miau!"
    
    def miar(self):
        return "Meow meow!"
    
c = Cachorro("Toto")
g = Gato("Pipoca")
print(f"{c.nome} fala: {c.emitir_som()}")
print(f"{c.nome} tambem fala: {c.latir()}")
print(f"{g.nome} fala: {g.emitir_som()}")
print(f"{g.nome} tambem fala: {g.miar()}")