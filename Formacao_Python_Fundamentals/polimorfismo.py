#Explorando polimorfismo com herança

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal voa")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_de_voo(passaro):
    passaro.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())

#note que chamamos o metodo voar() para ambas as classes, porem tem resultados
#diferentes