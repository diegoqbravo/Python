#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sin títulasdo.py


###funcion
def funcion(a,b):
	if(a != 0):
		print("primera solucion:", - b / a);
	elif ((a == 0) and (b == 0)):
		print("solucion para ambos");
	elif ((a == 0) and (b != 0)):
		print("sin solución");
	else:
		return;
###toma de datos
def main():
	a = int(raw_input("Ingrese a: "));
	b = int(raw_input("Ingrese b: "));
	x=funcion(a,b); #entrego los datos la funcion
	return x;#regreso a la funcion
main();
raw_input();
