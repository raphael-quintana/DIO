numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)

letras = set("abacaxi")
print(letras)

carros = set({"palio", "gol", "celta", "palio"})
print(carros)

linguagens = {"python", "java", "python"}
print(linguagens)

#Lembrando que não podemos confiar na ordem

#Para acessar os dados, precisamos converter o set em uma lista.


numeros = list(numeros)
print(numeros[0])


for carro in carros:
    print(carro)

#Para saber o indice que estamos percorrendo com o for, 
# podemos usar a função enumerate


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


#Set são coonjuntos matemáticos, logo, temos módulos para calcular união, 
#intersecção, diferença e diferença simétrica

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.union(conjunto_b))

print(conjunto_a.intersection(conjunto_b))

print(conjunto_a.difference(conjunto_b))

print(conjunto_b.difference(conjunto_a))

print(conjunto_a.symmetric_difference(conjunto_b))

#Também podemos trabalhar com subconjuntos 

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))

print(conjunto_b.issuperset(conjunto_a))

#Também podemos trabalhar com conjuntos disjuntos

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

#Tambem temos os modulo para adicionar ou remover elementos.

sorteio = {1, 23}

sorteio.add(25)
sorteio.add(45)
sorteio.add(45)

print(sorteio)

#Clear limpa seu conjunto, copy copia seu set

print(sorteio)
sorteio.clear()

sorteio = {1, 23}
sorteio.copy()

print(sorteio)

#Discard para remover do set, se n'ao existir ele segue.
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0,}

print(numeros)
numeros.discard(1)

print(numeros)

#Pop para ir removendo os items do set por ordem do indice
numeros.pop()
print(numeros)
numeros.pop()
print(numeros)


#Remove tambem remove do set, mas dá erro se não existir

numeros.remove(9)
print(numeros)
print(len(numeros))

