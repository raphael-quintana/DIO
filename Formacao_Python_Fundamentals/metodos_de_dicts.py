#explorando os métodos dos dicionários

contatos = {
    "jill@gmail.com": {"nome": "Jill", "ID": 44768},
    "chris@gmail.com": {"nome": "Chris", "ID": 44758},
    "leon@gmail.com": {"nome": "Leon", "ID": 44799},
    "claire@gmail.com": {"nome": "Claire", "ID": 9999},
}


#O método clear para limpar todos os valores do dicionário
contatos.clear()

print(contatos)


contatos = {
    "jill@gmail.com": {"nome": "Jill", "ID": 44768},
    "chris@gmail.com": {"nome": "Chris", "ID": 44758},
    "leon@gmail.com": {"nome": "Leon", "ID": 44799},
    "claire@gmail.com": {"nome": "Claire", "ID": 9999},
}

#O método copy() para copiar o dicionário em outro endereço de memória.

copia = contatos.copy()

print(copia["jill@gmail.com"]["nome"])

print(id(contatos))
print(id(copia))


#o método fromkeys() te permite criar chaves no seu dicionário, podendo ser vazia
#ou não

dict.fromkeys(["nome", "telefone"]) # Criar somente as chaves com o valor None

dict.fromkeys(["nome", "telefone"], "vazio") # Aqui você cria as chaves da lista
#e adiciona o valor "vazio" nas chaves.

#O método get é uma outra forma de acessar valores do seu dicionário. porém, sem
#risco de parar o programa

contatos = {
    "jill@gmail.com": {"nome": "Jill", "ID": 44768},
    "chris@gmail.com": {"nome": "Chris", "ID": 44758},
    "leon@gmail.com": {"nome": "Leon", "ID": 44799},
    "claire@gmail.com": {"nome": "Claire", "ID": 9999},
}

#print(contatos["chave"]) #Key Error

#Note que acessando uma chave que não existe no dict, ele acusa o key error.
# Se usarmos o método get(), ele fala que não tem a chave e vida que segue.

print(contatos.get("chave"))

print(contatos.get("chave", {})) # Nesse caso, enviamos as chaves como valor
#default, logo, como ele não encontrou a chave solicitada, retornou o valor default.

print(contatos.get("leon@gmail.com", {}))


#Com o método items, ele nos retorna uma lista de tuplas com os items do dict.

print(contatos.items())


#No caso do método keys, ele nos retorna uma lista com as chaves do dict.

print(contatos.keys())

#Com o método pop(), podemos remover as chaves do nosso dict.

print(contatos.pop("claire@gmail.com")) #Podemos colocar um segundo argumento caso
#você não tenha certeza se a chave existe ou não no dict, para evitar erros.

print(contatos)

#Com o método popitem(), ele remove as chaves e seus valores em sequencia

print(contatos.popitem())

print(contatos)

#Com o método setdefault(), caso ele encontre o item no dict, ele retorna o item.
#Caso não encontre, ele cria com o valor que colocamos como argumento.

contatos = {
    "jill@gmail.com": {"nome": "Jill", "ID": 44768},
    "chris@gmail.com": {"nome": "Chris", "ID": 44758},
    "leon@gmail.com": {"nome": "Leon", "ID": 44799},
}

contatos.setdefault("nome", "Claire")
print(contatos)

contatos.setdefault("idade", 26)
print(contatos)

#Com o método update(), podemos atualizar as chaves e valores do nosso dict.


contatos = {
    "jill@gmail.com": {"nome": "Jill", "ID": 44768},
    "chris@gmail.com": {"nome": "Chris", "ID": 44758},
    "leon@gmail.com": {"nome": "Leon", "ID": 44799},
}

contatos.update({"chris@gmail.com": {"nome": "Pamonha", "ID": 696913}})
print(contatos)

#Com o método values(), ele retorna os valores das chaves do dict.

print(contatos.values())

#Com o método in, podemos verificar se a chave já existe no dict.

jill = "jill@gmail.com" in contatos
print(jill)

jill2 = "nome" in contatos["jill@gmail.com"] # Note que aqui estamos dentro do segundo dict.
print(jill2)

#Com o método del(), ele retira o valor seja da chave, ou do valor que indicarmos

del contatos["chris@gmail.com"]["ID"]
del contatos["jill@gmail.com"]["ID"]
del contatos["leon@gmail.com"]["ID"]

print(contatos)