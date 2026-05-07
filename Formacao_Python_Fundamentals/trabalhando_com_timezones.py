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
from datetime import datetime

data = datetime.now(pytz.timezone("Europe/Oslo"))
print(data)

