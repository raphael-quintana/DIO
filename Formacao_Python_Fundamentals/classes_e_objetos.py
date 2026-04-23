#explorando classes e objetos


#classe
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Ruff")

    def dormir(self):
        self.acordado = False
        print("ZZZzzz...")


#Objeto

cao_1 = Cachorro("Chappie", "Amarelo", False)
cao_2 = Cachorro("Alladim", "Branco e Preto")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)


