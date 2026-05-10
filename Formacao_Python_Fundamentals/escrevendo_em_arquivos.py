#Exlorando a escrita em arquivos com o write() ou writelines()


#Lembre de abrir o arquivo no modo correto!

file = open("DIO/Formacao_Python_Fundamentals/example.txt", "w")

file.write("Escrevendo em dados em um novo txt.")

file.writelines(["\n", "escrevendo", " ", "um", " ", "novo", " ", "texto."])

file.close()