#Explorando classes abstratas com o modulo abc

#Abstract Based Class - ABC Module


#Deixando a classe abstrata, ela funciona como um manual de instrucoes para a
#criação, e abstraindo os métodos, você obriga a criação de novos na instancia
#criada.

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")

    def desligar(self):
        print("Desligando a TV")


controle = ControleTV()
controle.ligar()
controle.desligar()

