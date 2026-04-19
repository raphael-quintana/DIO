#Explorando Listas

#Criação e acesso aos dados

frutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("python")
print(letras)
print(type(letras))

numeros = list(range(10))
print(numeros)
print(type(numeros))

carro = ["Ferrari", "F8", 130000, 2020, "São Paulo", True]

print(type(carro))

#Note que podemos adicionar diversos tipos de dados na mesma lista

#Podemos fazer o acesso direto aos valores da lista pelo numero do indice

frutas = ["laranja", "maca", "uva"]
print(frutas[0])
print(frutas[2])

#Lembrando que podemos também usar o índice negativo para acessar os valores
print(frutas[-1])
print(frutas[-3])


#Também podemos fazer o aninhamento de listas para fazer a representação de
#matrizes

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

#Lembrando que a matriz é acessada por linha e coluna
print(matriz[0]) 
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

#Slicing(fatiamento) é interessante para acessar um conjunto de valores
#de uma lista pelo indice, e podemos tambem usar o te

print(letras)

print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])


#Utilizando o for, podemos passar por toda a lista
for letra in letras:
    print(letra)


#Podemos usar a função enumarate para pegar contar o indice do laço for.

for indice, letra in enumerate(letras):
    print(f"{indice}: {letra}")


#Com a compreensão de listas, podemos criar uma nova lista com base nos valores
#de alguma lista já existente. No exemplo, pegamos os valores pares verificando
# se o resto da divisão por 2 é igual à zero.

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)


# No caso do list comprehension, podemos deixar esse código mais performático,
#adicionando o valor de return(primeiro numero), aplicamos o for, e se True,
#ele retorna o valor par.

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)


#Podemos também modificar valores, aqui utilizando o for, criamos uma lista
#dos quadrados dos elementos da lista numeros.

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)


#Podemos também fazer tudo na mesma linha, para deixar mais performático.

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]

print(quadrado)


