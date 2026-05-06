#Explorando a conversão e formatação de datas e horas

#O Python permite a conversão de datas e horas. Para isso usamos os métodos
# "strftime" (string format time) e "strptime" (string parse time).

#Exemplo

import datetime

d = datetime.datetime.now()

#Formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M"))

#Convertendo string para datetime
date_string = "21/06/1991 20:00"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)

#Exemplo 2

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "1991-04-27 20:00"
mascara_ptbr = "%d/%m/%Y %H:%M %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))