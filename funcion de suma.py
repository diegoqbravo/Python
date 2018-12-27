#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  funcion de suma.py

def suma(a,b,c,d,e):
	sumaTotal=a+b+c+d+e;
	return sumaTotal;
def imprimir():
	a=int(raw_input("Ingrese numero: "));
	b=int(raw_input("Ingrese numero: "));
	c=int(raw_input("Ingrese numero: "));
	d=int(raw_input("Ingrese numero: "));
	e=int(raw_input("Ingrese numero: "));
	imprime=suma(a,b,c,d,e);
	print"el resultado es: ", imprime;
def main():
	imprimir();
main();
