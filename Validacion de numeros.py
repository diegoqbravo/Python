#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Validacion de numeros.py
def validacion(a,b,c):
	if((a<b)and(a<c)):
		print("A es Menor que B y C");
	elif((a==b)and(a==c)):
		print("A, B y C son Iguales");
	elif((b<a)and(b<c)):
		print("B es menor que A y C");
	else:
		print("C es menor que A y B");
def ingreseDatos():
	a=int(raw_input("Ingrese A Numero: "));
	b=int(raw_input("Ingrese B Numero: "));
	c=int(raw_input("Ingrese C Numero: "));
	d=validacion(a,b,c); ##aqui le doy los datos a validacion
def main():
	ingreseDatos();
main();
