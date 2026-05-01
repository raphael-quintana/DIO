#Explorando data, hora e fuso no Python

import datetime

d = datetime.date(2023, 7, 19)
print(d)

#podemos tambem usar o from, para selecionar o objeto date da classe datetime.

from datetime import date, datetime, time

data = date(2025, 6, 21)
print(data)

print(date.today()) #Com o método today(), podemos pegar a data atual.

#No caso da classe datetime, temos que prover além dos argumentos básicos como
#dia, mês e ano. Mas também argumentos como hora, min, seg e miliseg.
#Novamente, usando o módulo today(), pegamos a data atual.

print(datetime.today())

data2 = datetime(1991, 6, 21, 20, 30, 45)
print(data2)

#lembrando que se omitirmos as horas, ele irá fazer o print com elas zeradas

data2 = datetime(1991, 6, 21)
print(data2)

#Podemos usar também o objeto time, correspondente somente às horas

horas = time(12, 30, 45)
print(horas)

print(time)
