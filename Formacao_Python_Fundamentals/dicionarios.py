#Explorando dicionários

#Lembrando que dicionários são conjuntos de pares chave-valor. repŕesentado por
# {}.

pessoa = {"nome": "Raphael", "idade": 35}

pessoa = dict(nome="Guino", idade=11)

pessoa["telefone"] = "11-942514165"

print(pessoa)

#Para acessar os dados, podemos usar o nome da chave em colchetes[]

dados = {"nome": "Raphael", "idade": 34, "telefone": "11942514165"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

#Com a mesma sintaxe, podemos alterar os valores, indexando pelo nome da chave

dados["idade"] = 11
dados["nome"] = "Guino"
print(dados)

#Os dicionários também aceitam aninhamento, podendo armazenar um dicionário dentro
#de outro dicionário. Com a única condição de que a chave sempre seja imutável.

contatos = {
    "jill@gmail.com": {"nome": "Jill", "ID": 44768},
    "chris@gmail.com": {"nome": "Chris", "ID": 44758},
    "leon@gmail.com": {"nome": "Leon", "ID": 44799},
    "claire@gmail.com": {"nome": "Claire", "ID": 9999},
}

print(contatos["chris@gmail.com"]["ID"])


