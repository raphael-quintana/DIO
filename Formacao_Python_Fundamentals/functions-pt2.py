#Explorando funções com argumentos posicionais, argumentos nomeados e mistos.

#No caso de mistos devemos seguir a ordem
#def criar_carro(posicionais, /, posicionais ou keywords, *, somente keywords)

#No caso abaixo, começando com posicionais e depois da barra, podemos ter keywords.

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina") #válido

#Também podemos criar uma função com argumentos keyword only

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina")

#Funções também são objetos de primeira classe, como listas, tuplas, dicts, etc.
#Logo, podemos usar uma função como variável, passar uma função como parametro
#para outra função. Usar como valor em estruturas de dados. e usar como valor de 
#return também.

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(30, 30, somar)

#Dentro do escopo local e global, podemos usar uma variavel global dentro de uma
#função, somente indicando que ela é global para a função. HORRIVEL PARA MANTER
#O CODIGO. NÃO É BEST PRACTICES USAR.

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))

