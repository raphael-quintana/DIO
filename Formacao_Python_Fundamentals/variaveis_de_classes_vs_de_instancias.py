#Explorando as diferenças das variáveis das classes, e das variáveis das 
#instâncias

class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} ({self.numero} - {self.escola})"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

e1 = Estudante("Raphael", 4165)
e2 = Estudante("Toninho", 4251)

mostrar_valores(e1, e2)

e2.numero = 1666

mostrar_valores(e1, e2)

#Note que lidamos até então somente com os atributos(variaveis) das instancias,
#caso alteremos algum que está na classe, ele alterará para todas as instancias,
#mesmo que criemos uma nova.


Estudante.escola = "Python"

e3 = Estudante("Ivo", 2704)

mostrar_valores(e1, e2, e3)


