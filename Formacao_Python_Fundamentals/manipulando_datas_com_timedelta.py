#Maniplando datas com timedelta

#Para efetuar algumas manipulações em datas, utilizamos objetos timedelta, que
#representam uma duração, a diferença entre duas datas ou horas.

#Exemplo

import datetime

#Criando data e hora
d = datetime.datetime(2023, 7, 19, 13, 45)
print(d)

#Adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d)


#exemplo 2

from datetime import date, time , datetime, timedelta


tipo_carro = "M" #P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()


if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual}, e ficará pronto às {data_estimada}.")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual}, e ficará pronto às {data_estimada}.")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual}, e ficará pronto às {data_estimada}.")


#Exemplo 3

print(date.today() - timedelta(days=1))

resultado = datetime(2025, 5, 6, 19, 50, 20) - timedelta(hours=1)
print(resultado.time())