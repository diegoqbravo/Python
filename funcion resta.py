#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  funcion de suma.py

def resta(a,b,c,d,e):
	restaTotal=a-b-c-d-e;
	return restaTotal;
def imprimir():
	a=int(raw_input("Ingrese numero: "));
	b=int(raw_input("Ingrese numero: "));
	c=int(raw_input("Ingrese numero: "));
	d=int(raw_input("Ingrese numero: "));
	e=int(raw_input("Ingrese numero: "));
	imprime=resta(a,b,c,d,e);
	print"el resultado es: ", imprime;
def main():
	imprimir();
main();
