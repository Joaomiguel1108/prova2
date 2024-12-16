class Leão:
    def falar(self):
        print("Rugido")

class Lobo:
    def falar(self):
        print("Uivo!")

class Arara:
    def falar(self):
        print("Olá!")

class Carro:
    pass  


def executar_acao(objeto):
    if hasattr(objeto, 'falar'): 
        objeto.falar()
    else:
        print("Erro: O objeto não possui o método 'falar'.")

arara = Arara()
leão = Leão()
lobo = Lobo()
carro = Carro()


executar_acao(arara)  
executar_acao(leão)      
executar_acao(lobo)
executar_acao(carro)    


13) # Erro: AttributeError: 'Carro' object has no attribute 'falar'
