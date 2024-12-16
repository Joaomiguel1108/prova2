class Leão:
    def falar(self):
        print("Rugido")

class Lobo:
    def falar(self):
        print("Uivo!")

class Arara:
    def falar(self):
        print("Olá!")

arara = Arara()
leão = Leão()
lobo = Lobo()

arara.falar()
leão.falar()
lobo.falar()


9)
Quando dois objetos de classes diferentes possuem métodos com o mesmo nome, cada método será executado de acordo com a implementação de sua respectiva classe. Isso caracteriza o polimorfismo, onde o mesmo nome de método (falar) realiza ações distintas dependendo do objeto que o invoca.
