class Veiculo:
    def mover(self):
        pass  

class Carro(Veiculo):
    def mover(self):
        print("Au au!")

class Moto(Veiculo):
    def mover(self):
        print("Miau!")

class Caminhão(Veiculo):
    def mover(self):
        print("Olá!")

class Patinete(Veiculo):
    def mover(self):
        print("Patinetes deslizam")

carro = Carro()
moto= Moto()
caminhão = Caminhão()
patinete = Patinete()


veiculos = [carro, moto, caminhão, patinete]

for Veiculo in veiculos:
    Veiculo.mover()

#19)
'''A herança facilita o polimorfismo porque permite:

Definir uma interface comum: A classe base Animal define o método falar() que todas as subclasses implementam de maneira diferente.
Tratamento uniforme dos objetos: Podemos manipular todos os objetos das subclasses (Cachorro, Gato, Papagaio) como se fossem do tipo Animal. Assim, a lista animais contém objetos diferentes, mas podemos chamá-los uniformemente usando o método falar().
Facilidade de expansão: Caso precisemos adicionar novos tipos de animais, como Peixe, basta criar uma nova classe que herde de Animal e sobrescreva o método falar(). O código que utiliza a classe base (Animal) continua funcionando sem mudanças.'''
