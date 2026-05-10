#Explorando a manipulação de arquivos em Python. Vamos trabalhar com txt e csv.

#Abrindo e fechando arquivos

#Para abrir arquivos, usamos a função open(). Quando terminamos de trabalhar
#com o arquivo, usamos a função close() para liberar recursos.

#Existem diferentes modos para você abrir um arquivo, como somente leitura("r"),
#gravação("w") e anexar("a"). O modo deve ser escolhido de acordo com a operação
#que vamos realizar.

file = open("/home/raphael-quintana/Workspace/DIO/Formacao_Python_Fundamentals/listas.py", "r")

file.close()

#Leitura de arquivos em Python.

# O Python fornece várias maneiras de ler um arquivo. Podemos usar read(),
#readline() ou readlines() dependendo da necessidade.

file = open("/home/raphael-quintana/Workspace/DIO/Formacao_Python_Fundamentals/listas.py", "r")
print(file.read())
file.close()

#No caso do readline(), ele le uma linha por vez, e readlines() le uma lista onde
#cada elemento é uma linha do arquivo.

file = open("/home/raphael-quintana/Workspace/DIO/Formacao_Python_Fundamentals/listas.py", "r")
print(file.readline())
file.close()

#Mostrando todas as linhas usando o laço for

file = open("/home/raphael-quintana/Workspace/DIO/Formacao_Python_Fundamentals/listas.py", "r")
for linha in file.readline():
    print(linha)
file.close()

#Também podemos iterar pelas linhas do arquivo com o while

file = open("/home/raphael-quintana/Workspace/DIO/Formacao_Python_Fundamentals/listas.py", "r")
while len(linha := file.readline()):
    print(linha)
file.close()


#Usando readlines()
file = open("/home/raphael-quintana/Workspace/DIO/Formacao_Python_Fundamentals/listas.py", "r")
print(file.readlines())
file.close()


