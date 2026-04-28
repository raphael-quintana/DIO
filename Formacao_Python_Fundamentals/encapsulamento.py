#Explorando encapsulamento em Python

#Objeto Publico: Só pode ser acessado de fora da classe
#Objeto Privado: Só pode ser acessado pela classe

#objeto = publico

#_objeto = privado

class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo #Note que o saldo está privado
    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self): #Note que criamos o método mostrar saldo para poder
        return self._saldo    #mostrar o saldo da conta para quem tem autorização
                                #sem manipular a variável privada.
    

conta = Conta(100)
conta.depositar(500)
conta.sacar(300)
    
print(conta.mostrar_saldo())
