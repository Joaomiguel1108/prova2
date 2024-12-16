#24)
#Se tentarmos criar diretamente um objeto da classe abstrata Forma, o Python lançará um erro TypeError, pois não é permitido instanciar classes abstratas com métodos abstratos não implementados.


from abc import ABC, abstractmethod
import math


class Forma(ABC):
    @abstractmethod
    def perimetro(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def perimetro(self):
        return (3.14*2)*self.raio 

class TrianguloEquilatero(Forma):
    def __init__(self, lado):
        self.lado = lado
        
    def perimetro(self):
        return self.lado * 3


quadrado = Quadrado(5)
circulo = Circulo(4)
triangulo = TrianguloEquilatero(6)

print(f"perimetro do quadrado: {quadrado.perimetro()}")  
print(f"perimetro do círculo: {circulo.perimetro():.2f}")  
print(f"perimetro do triângulo equilatero: {triangulo.perimetro()}")  
