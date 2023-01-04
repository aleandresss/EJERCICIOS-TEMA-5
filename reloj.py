#desarrollar un reloj de horas, minutos y segundos - módulo datetime con la hora actual-  Hazlo en un script llamado reloj.py y ejecútalo en la terminal:

from datetime import datetime as dt #libreria de tiempo
import time
import os

now = dt.now()
hora = now.hour
minuto = now.minute
segundo =  now.second

while True:
    os.system("cls")
    print(f"{hora:02d}:{minuto:02d}:{segundo:02s}")
    segundo+=1
    if segundo > or = 60: 
         minuto += 1 #sumamos 1, resultado se almacena en la variable antes del signo 
        segundo=0 
        if minuto > or = 60: #60 seg = 1min
            hora += 1       
            minuto=0
            if hora > or = 24: #1dia = 24h
                hora = 0 
    time.sleep(1)
