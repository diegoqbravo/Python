#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  año.py

def funcion(fecha1, fecha2):
	if fecha1 - fecha2 == 1:
		print("Desde el anho", fecha2, "ha pasado 1 año");
	elif fecha1 > fecha2:
		print("Desde el anho", fecha2, "a pasado", fecha1 - fecha2, "años");
	elif fecha1 - fecha2 == -1:
		print("para llegar", fecha2, "falta 1 año");
	elif fecha1 < fecha2:
		print("para llegar", fecha2, "faltan", fecha2 - fecha1, "años");
	else:
		print("Mismo Año");
def main():
	fecha1 = int(raw_input("Ecriba el Anho Actual: "));
	fecha2 = int(raw_input("Escriba Cualquier Anho: "));
	nFecha=funcion(fecha1, fecha2);#entrego los datos
	return nFecha;#regreso a la funcion
main();


