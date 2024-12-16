1)#Polimorfismo é um conceito da programação orientada a objetos que permite que métodos com o mesmo nome possam se comportar de maneiras diferentes, dependendo da classe em que são implementados. Em outras palavras, um mesmo método pode ter várias formas, adaptando-se ao objeto que o invoca. Ele é útil para aumentar a flexibilidade e reutilização de código
2)
class Pessoa:
    def mover(self):
    pass

class Objeto:
    def mover(self):
    pass
3)
pessoa = Pessoa()
objeto = Objeto()

pessoa.executar()
objeto.executar()

4)
class Pessoa:
    def mover(self):
        

class Objeto:
    def mover(self):

pessoa = Pessoa()
objeto = Objeto()

pessoa.executar()
objeto.executar()

5)
Ao tentar chamar o método mover() sem implementação (ou seja, usando o pass), nada acontecerá visivelmente. Isso ocorre porque o método existe, mas não contém nenhuma lógica ou instrução a ser executada.
