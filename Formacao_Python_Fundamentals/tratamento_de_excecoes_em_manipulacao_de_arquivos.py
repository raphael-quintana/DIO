#Tratar erros é uma parte importante da manipulação de arquivos. O Python oferece
#uma série de exceções que nos permitem lidar com erros comuns.

#Exceções mais comuns

#FileNotFoundError: Lançada quando o arquivo que está sendo aberto não pode
#ser encontrado no diretório especificado.

#PermissionError: Lançada quando ocorre uma tentativa de abrir um arquivo sem
#as permissões adequadas para leitura ou gravação.

#IOError: Lançada quando ocorre um erro geral de E/S (entrada/saída) ao trabalhar
#com o arquivo, como problemas de permissão, falta de espaço em disco, entre outros.

#UnicodeDecodeError: Lançada quando ocorre um erro ao tentar decodificar os
#dados de um arquivo de texto usando uma codificação inadequada.

#UnicodeEncodeError: Lançada quando ocorre um erro ao tentar codificar dados
#em uma determinada codificação ao gravar em um arquivo de texto.

#IsADirectoryError: Lançada quando é feita uma tentativa de abrir um diretório
#em vez de um arquivo de texto.

from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    file = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")


