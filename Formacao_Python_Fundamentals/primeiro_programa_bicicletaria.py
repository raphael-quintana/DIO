#Iniciando o promeiro programa baseado em objetos. Projeto DIO



#Criei uma classe chamada Bicicleta, com os atributos e comportamentos esperados

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzina(self):
        print("Beep Beep!")
        
    def parar(self):
        print("Aperta o freio!")

    def correr(self):
        print("Acelerando!")

    def __str__(self):
        return f"{self.__class__.__name__}:{", ".join([f"{chave}={valor}"
for chave, valor in self.__dict__.items()])}"
    
#Agora vamos criar os objetos

bike_1 = Bicicleta("Vermelho", "BMX", 2000, 500)
bike_2 = Bicicleta("Vermelho", "Monark", 2000, 200)
bike_3 = Bicicleta("Azul", "MB", 2000, 900)

print(bike_2)
print(bike_3)