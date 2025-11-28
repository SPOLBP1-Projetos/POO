class Veiculo: # classe mãe
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")


class Carro(Veiculo): # classe filha
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo) # esse super serve para que em vez de repetir código, chamamos o método da classe mãe e depois acrescentamos as informações extras.
        self.num_portas = num_portas # nesse caso, o número de portas é um atributo específico da classe Carro, mas obviamente não seria da classe Moto por exemplo.

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Número de portas: {self.num_portas}")
        print("-" * 30)


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Cilindradas: {self.cilindradas} cc")
        print("-" * 30)

# objetos de Carro e Moto
carro1 = Carro("Toyota", "Corolla", 4)
moto1 = Moto("Honda", "CB 500F", 500)

carro1.exibir_detalhes()
moto1.exibir_detalhes()
