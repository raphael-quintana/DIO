#Explorando heranças em Python

class Veículo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return self.cor
    

class Motocicleta(Veículo):
    pass

class Carro(Veículo):
    pass

class Caminhao(Veículo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado


    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Nao"}")


moto = Motocicleta("Preta", "ABC123", 2)
moto.ligar_motor()
print(moto)


carro = Carro("Verde", "ABC123", 4)
carro.ligar_motor()
print(carro)

caminhao = Caminhao("Azul", "ABC123", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)


#Explorando heranças múltiplas

class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
       
    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for 
        chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        
        

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
        
        

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass



gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="Vermelho", cor_bico="Laranja")
print(ornitorrinco)

print(Ornitorrinco.__mro__)
print(Gato.__mro__)

print(Ornitorrinco.mro())
#Method Resolution Order - Ordem de Resolução de Métodos

