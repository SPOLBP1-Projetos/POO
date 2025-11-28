class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.num_paginas}")
        print("-" * 30)

livros = [
    Livro("Dom Casmurro", "Machado de Assis", 256),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96),
    Livro("1984", "George Orwell", 328)
]

for livro in livros:
    livro.detalhes()
