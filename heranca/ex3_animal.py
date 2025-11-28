class Animal:
    def __init__(self, nome: str):
        self.nome = nome
    
    def emitir_som(self):
        return "som generico"
    
class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au!"
    
    def latir(self):
        return "Woof woof!"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
    def miar(self):
        return "Meow meow!"
    

dog = Cachorro("Toto")


cat = Gato("Pipoca")


print(f"{dog.nome} fala: {dog.emitir_som()}")
print(f"{dog.nome} tambem fala: {dog.latir()}")

print(f"{cat.nome} fala: {cat.emitir_som()}")
print(f"{cat.nome} tambem fala: {cat.miar()}")