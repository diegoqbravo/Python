#!/usr/bin/env python
# -*- coding: utf-8 -*-

#a=int(raw_input("Ingrese primer numero: "));
#b=int(raw_input("Ingrese segundo numero: "));
def division(a,b):
	if(b==0):
		print("no se puede dividir en 0")
		return;
	else:	
		c=a/b;
		return c;
				
def imprime():
	a=int(raw_input("Ingrese primer numero: "));
	b=int(raw_input("Ingrese segundo numero: "));
	imprimir=division(a,b);
	print"el resultado es: ", imprimir;
def main():
	imprime();
main();
