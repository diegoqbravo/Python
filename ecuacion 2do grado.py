#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Ecuacion 2doGRADOjiiiii.py

	
##esta es la funcion
def funcion(a,b,c):
	d = b*b - 4*a*c;
	if (a == b == c == 0):
		print("Todos son Solucion");
	elif ((a == b == 0) and (c != 0)):
		print("Sin solución");
	elif ((a == 0) and (b != 0) and (c != 0)):
		print("1 solucion:", -c / b);
	elif ((a !=0) and (d < 0)):
		print("Error no Solucion");
	elif ((a !=0) and (d == 0)):
		print("Una Solucion", -b / (2*a));
	elif ((a !=0) and (d > 0)):
		print("2 Soluciones:", (-b - d**0.5) / (2*a), "y", (-b + d**0.5) / (2*a));
	else:
		return;
def main():
	a = int(raw_input("ingrese a: "));
	b = int(raw_input("ingrese b: "));
	c = int(raw_input("ingrese c: "));
	x=funcion(a,b,c);#entrego los datos a la funcion
	return x;#regreso a la funcion
main();
raw_input();
