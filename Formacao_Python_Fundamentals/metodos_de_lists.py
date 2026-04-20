#Explorando os métodos que podemos usar com as listas.

#Podemos adicionar elementos na lista pelo método append. Lembrando que elas
#aceitam qualquer objeto.

lista = []

lista.append(1)
lista.append("python")
lista.append([30, 40, 50])

print(lista)

#Para limpar a lista, podemos usar o método clear()

lista.clear()
print(lista)

#Com o método copy, ele retorna uma cópia da lista, porem com outro endereço de
#memória. Podemos verificar com a função id(), que exibe o endereço de memória
#da variável.

lista = [1, "python", [30, 40 ,50]]

lista_2 = lista.copy()

print(lista)
print(lista_2)

print(id(lista))
print(id(lista_2))

#Usamos o método count para contas quantas vezes aparece um certo objeto
#dentro da lista

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

#Podemos usar o método extend para extender uma lista já com outra lista, evitando
#o uso do append, que vai de um em um. Ele adiciona todo mundo, independente de 
# duplicar ou não.

linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])

print(linguagens)

#Com o método index(), conseguimos saber qual é a posição no indice da primeira
#ocorrência do objeto na lista.

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))
print(linguagens.index("python"))


#Por padrão, a lista funciona como um empilhamento de objetos, então podemos
#usar o método pop(), para remover sempre o último item adicionado na lista,
#a não ser que você passe o índice para ele

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())
print(linguagens)

print(linguagens.pop())
print(linguagens)

print(linguagens.pop())
print(linguagens)

print(linguagens.pop(0))
print(linguagens)


#No caso do método remove(), ele pede o objeto em si, e não o índice do objeto.
#Lembrando que ele irá remover uma ocorrência por vez, caso o objeto apareça
#mais de uma vez na lista.

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.remove("python"))
print(linguagens)

#Com o método reverse, nós invertemos a ordem dos objetos na lista, espelhando a 
#lista.

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens)


linguagens.reverse()
print(linguagens)


#Usamos o método sort() para ordenar a lista em ordem alfabética.

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print(linguagens)

#Colocando o argumento reverse=True para inverter a ordem da lista

linguagens.sort(reverse=True)
print(linguagens)

#Colocando o argumento key, adicionamos uma função anônima, para ordenar em ordem
#crescente em numero de caracteres.

linguagens.sort(key=lambda x: len(x))
print(linguagens)

#Podemos também usar os 2 argumentos ao mesmo tempo.

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

#Usando a função built-in chamada sorted, podemos fazer o mesmo que o método sort.

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))



