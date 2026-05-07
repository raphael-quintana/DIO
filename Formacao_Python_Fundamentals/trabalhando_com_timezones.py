#Trabalhando com timezones

#Lidar com fusos horários é uma necessidade comum. O Python facilita isso
#através do módulo pytz.

import datetime
import pytz

#Criando datetime com timezone
d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d)

d = datetime.datetime.now(pytz.timezone("America/Toronto"))
print(d)

d = datetime.datetime.now(pytz.timezone("America/Los_Angeles"))
print(d)


#Exemplo
import pytz
from datetime import datetime, timezone, timedelta

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Vancouver"))
print(data)
print(data2)



#Podemos também criar um objeto timezone sem o pytz

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sp = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sp)