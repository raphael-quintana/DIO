#Explorando Tuplas

#No caso das lista, que é representada por [] e mutável. A tupla é representada
#por (), separando valores por , e imutável. Não podendo alterar os valores.

frutas = ("laranja", "pera", "uva",)
print(frutas)
print(type(frutas))

letras = tuple("python")
print(letras)
print(type(letras))

numeros = tuple([1, 2, 3, 4])
print(numeros)
print(type(numeros))

pais = ("Brasil",)
print(pais)
print(type(pais))

#Para evitar erros no runtime do Python, quando usar tuplas, deixar uma vírgula,
#para o Python não achar que é precedência dos operadores.

#Para acessar os dados das tuplas, é o mesmo das listas

frutas = ("laranja", "pera", "uva", "maça",)

print(frutas[1])
print(frutas[0])
print(frutas[-1])
print(frutas[-3])

#Também podemos fazer aninhamento com tuplas.

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

#Lembrando que a matriz é acessada por linha e coluna
print(matriz[0]) 
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

#O mesmo vale para o slicing

print(letras)

print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])