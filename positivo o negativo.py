#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  positivo o negativo.py


def posneg(a):
	if(a>0):
		print("numero es positivo");
	elif(a<0):	
		print("el numero es negativo");
	else:
		print("el numero es 0");				
def imprime():
	a=int(raw_input("Ingrese numero: "));
	imprimir=posneg(a);
def main():
	imprime();
main();
