# Mostrar en pantalla los meses transcurridos desde la fecha de nacimiento de un usuario

from datetime import date
from datetime import datetime
from datetime import timedelta

print("ingrese el año del nacomiento")
año=int(input())
print("Ingrese el mes de nacimieto")
mes=int(input())
print("Ingrese el dia de nacimiento")
dia=int(input())
nacimiento=datetime(año,mes,dia,00,00,00,00)
hoy=datetime.now()
dias = (hoy-nacimiento).days
meses=dias/30
print("han pasado ","{:.2f}".format(meses), " desde el nacimiento")