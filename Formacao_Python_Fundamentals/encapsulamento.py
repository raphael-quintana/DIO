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

#explorando properties no python

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property #A property transforma o metodo em propriedade, assim podemos usar a sintaxe de atributo.
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value

    @x.deleter
    def x(self):
        self._x = -1



foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)


#Explorando properties in another example

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento


    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa("Recruta", 2015)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")