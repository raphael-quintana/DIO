#Boas Praticas na Manipulação de arquivos.

#Bloco with: 

#Use o gerenciamento de contexto (context manager) com a declaração "with".
#O gerenciamento de contexto permite trabalhar com arquivos de forma segura,
#garantindo que eles sejam fechados corretamente, mesmo em casos de exceções.


from pathlib import Path

ROOT_PATH = Path(__file__).parent

#with open(ROOT_PATH / "example.txt", "r") as arquivo:
#    print("Trabalhando com o aquivo")
#
#print(arquivo.read())


#Verifique se o arquivo foi aberto com sucesso
#É recomendado verificar se o arquivo foi aberto corretamente antes de executar 
# operações de leitura ou gravação nele.

#try:
    #with open(ROOT_PATH / "example", "r") as arquivo:
    #    print(arquivo.read())

#except IOError as exc:
#    print(f"Erro ao abrir o arquivo: {exc}")


#Use a codificação correta

#Certifique-se de usar a codificação correta ao ler ou gravar arquivos de texto.
#O argumento "encoding" da função "open()" permite especificar a codificação.

#try:
#    with open(ROOT_PATH / "arquivo-utf-8.txt", "w",  encoding="utf-8") as arquivo:
#        arquivo.write("Aprendendo as manipular arquivos utilizando Python.")
#except IOError as exc:
#    print(f"Erro ao abrir o arquivo: {exc}")


try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r",  encoding="ascii") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except UnicodeDecodeError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")