#Explorando decoradores

#Passagem de parametros de referencia para as functions

def mensagem(nome):
    print(f"Executando mensagem")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("Executando mensagem longa")
    return f"Olá, tudo bem com você {nome}?"

def executar(function, nome):
    print("executando executar")
    return function(nome)


print(executar(mensagem, "Raph"))
print(executar(mensagem_longa, "Raph"))



#No caso do inner functions, ela só funciona quando chamada a principal primeiro.

def principal():
    print("executando a function principal")

    def inner_function():
        print("executando inner function")

    def inner_function_2():
        print("executando inner function 2")

    inner_function()
    inner_function_2()


principal()

#Tambem podemos retornar uma função de uma outra função

def calculadora(operacao):
    def soma(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mul(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    


    #Podemos usar o match para criar uma estrutura switch case, como em C.

    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div


  #  if operacao == "+":
   #     return soma
    #elif operacao == "-":
    #    return sub
    #elif operacao == "*":
    #    return mul
    #else:
    #    return div


#Note que ao fazer o print da função, ele indica qual a função principal está indicando.
print(calculadora("+"))
print(calculadora("-"))
print(calculadora("*"))
print(calculadora("/"))

op = calculadora("+")
print(op(2, 7))

op = calculadora("-")
print(op(2, 7))

op = calculadora("*")
print(op(2, 7))

op = calculadora("/")
print(op(2, 7))


#Utilizamos o decorador para decorar nossa função, que nada mais são que inner functions.

def meu_decorador(function):
    def envelope():
        print("faz algo antes de executar")
        function()
        print("faz algo depois de executar")

    return envelope

def ola_mundo():
    print("ola, mundo!")


ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

#O Python tambem permite que nos usemos os decoradores de um jeito mais simples
# com o simbolo @.

def meu_decorador(function):
    def envelope():
        print("faz algo antes de executar")
        function()
        print("faz algo depois de executar")

    return envelope

@meu_decorador
def ola_mundo():
    print("ola, mundo!")


ola_mundo()


#Funções de decoração com argumentos

#Podemos usar *args e **kwargs na função interna, com iso ela aceitará um numero
#arbitrário de argumentos posicionais e de palavras-chave

#Exemplo
#def duplicar(func):
#    def envelope(*args, **kwargs):
#        func(*args, **kwargs)
#        return func(*args, **kwargs)
#
#    return envelope
#
#@duplicar
#def aprender(tecnologia):
#    print(f"Estou aprendendo {tecnologia}!")
#
# aprender("Python")


#exemplo2

def meu_decorador(function):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        function(*args, **kwargs)
        print("faz algo depois de executar")

    return envelope

#Usando os args e kwargs, podemos aumentar o numero de argumentos da funcao decorada
@meu_decorador
def ola_mundo(nome, idade):
    print(f"ola, mundo {nome} e tenho {idade} anos!")


ola_mundo("John", 22)


#Decorador retornando valor da função decorada


def meu_decorador(function):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = function(*args, **kwargs)
        print("faz algo depois de executar")
        return resultado

    return envelope

#Usando os args e kwargs, podemos aumentar o numero de argumentos da funcao decorada
@meu_decorador
def ola_mundo(nome) :
    print(f"ola, mundo {nome}!")
    return nome.upper()

resultado = ola_mundo("John")




#Introspecção

#Introspecção é a capacidade de um objeto saber sobre seus próprios atributos
#em tempo de execução.


import functools

def meu_decorador(function):
    @functools.wraps(function)
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        function(*args, **kwargs)
        print("faz algo depois de executar")
        

    return envelope

@meu_decorador
def ola_mundo(nome) :
    print(f"ola, mundo {nome}!")


