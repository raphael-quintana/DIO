#Explorando iteradores e geradores

#Iteradores são objetos que são iteraveis, como listas, strings, sequencias no geral.

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[28, 122, 983]):
    print(i)

#Geradores são um tipo especial de iteradores, mas não armazenam todos os seus
#valores na memória.

#São definidos usando funções regulares, mas, ao invés de retornar valores usando
#return, utilizam "yield"

## Uma vez que um item gerado é consumido, ele é esquecido e não pode ser acessado
##novamente

##O estado interno de um gerador é mantido entre chamadas

##A execução de um gerador é pausada na declaração "yield" e retomada daí na próxima
##vez que ele for chamado.

#Exemplo
import requests

def fetch_products(api_url, max_pages=100):
    page = 1
    while page <= max_pages:
        response = requests.get(f"{api_url}?page={page}")
        data = response.json()
        for product in data["products"]:
            yield product
        if "next_page" not in data:
            break
        page +=1


#Uso do gerador
for product in fetch_products("http://api.example.com/products"):
    print(product["name"])