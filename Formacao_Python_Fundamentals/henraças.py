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