#Trabalhando com arquivos .CSV

#CSV é a sigla para "Comma Separated Values"

#O Python fornece um módulo chamado "CSV" para lidar facilmente.

import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

ID_COLUMN = 0
NAME_COLUMN = 1

# try:
#     with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["ID", "Nome"])
#         writer.writerow(["1", "Maria"])
#         writer.writerow(["2", "João"])
# except IOError as exc:
#     print(f"Deu ruim, toma o erro: {exc}")

# try:
#     with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as file:
#         reader = csv.reader(file)
#         for index, row in enumerate(reader):
#             if index == 0:
#                 continue
#             print(f"ID: {row[ID_COLUMN]}")
#             print(f"Name: {row[NAME_COLUMN]}")
# except IOError as exc:
#     print(f"Deu ruim, toma o erro: {exc}")


#Praticas recomendadas

#Usar csv.reader e csv.writer para manipular arquivos csv.

# Fazer o tratamento correto das exceções

#Ao gravar arquivos CSV definir o argumento newline="" no método "open"


#Usando o DictReader, ele entender que a primeira linha é o header.

try:
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader.fieldnames)
        # for row in reader:
        #     print(f"ID: {row["ID"]}")
        #     print(f"Name: {row["Nome"]}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")