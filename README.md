# POO
Exercicios propostos no slide envolvendo POO, Herança e Poliformismo.

### Conceitos Fundamentais:
1. Classe Círculo: <br>
- Atributos: raio (float) <br>
- Métodos: <b>calcular_area():</b> Retorna a área do círculo (π×raio2) e <b>calcular_perimetro():</b> Retorna o perímetro do círculo (2×π×raio). <br>
- Exercício: Crie objetos da classe Círculo com diferentes raios e imprima suas áreas e perímetros.

2. Classe Livro:
- Atributos: titulo (string), autor (string), num_paginas (int)
- Métodos: detalhes(): Imprime todos os detalhes do livro.
- Exercício: Crie uma lista de objetos Livro e imprima os detalhes de cada um.

### Herança

3. Classe Animal (superclasse) e Cachorro, Gato (subclasses):
- Animal: <br>
■ Atributo: nome (string) <br>
■ Método: emitir_som() (imprime um som genérico)
- Cachorro: <br>
■ Método emitir_som(): Imprime "Au au!".<br>
■ Método latir(): Imprime "Woof woof!".
- Gato: <br>
■ Método emitir_som(): Imprime "Miau!". <br>
■ Método miar(): Imprime "Meow meow!".

- Exercício: Crie objetos de Cachorro e Gato, chame os métodos emitir_som(), latir() (para cachorro) e miar() (para gato). Demonstre o
polimorfismo ao chamar emitir_som() em objetos de ambas as classes.

4. Classes Veiculo (superclasse) e Carro, Moto (subclasses):
- Veiculo: <br>
■ Atributos: marca (string), modelo (string) <br>
■ Método: exibir_detalhes(): Imprime a marca e o modelo.
- Carro: <br>
■ Atributo adicional: num_portas (int) <br>
■ Override do método exibir_detalhes() para incluir o número de portas.
- Moto: <br>
■ Atributo adicional: cilindradas (int) <br>
■ Override do método exibir_detalhes() para incluir as cilindradas.

- Exercício: Crie objetos de Carro e Moto e chame o método exibir_detalhes() em cada um.

### Polimorfismo

5. Interface (ou classe abstrata) FormaGeometrica e classes Retangulo, Triangulo:

- FormaGeometrica: <br>
■ Método abstrato calcular_area() <br>
■ Método abstrato calcular_perimetro()
- Retangulo: <br>
■ Atributos: base (float), altura (float) <br>
■ Implementa calcular_area() e calcular_perimetro().
- Triangulo: <br>
■ Atributos: lado1 (float), lado2 (float), lado3 (float) <br>
■ Implementa calcular_area() (pode usar a fórmula de Heron) e
calcular_perimetro().

- Exercício: Crie uma lista de objetos de Retangulo e Triangulo. Itere pela lista e chame
os métodos calcular_area() e calcular_perimetro() para cada forma,
demonstrando o polimorfismo.
