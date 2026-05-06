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

