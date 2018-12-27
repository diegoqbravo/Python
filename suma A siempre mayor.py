#!/usr/bin/env python
# -*- coding: utf-8 -*-

def suma(a,b):
	if a > b:
		x=a+b
		print"El mayor es A y el resultado es: ", x;
	else:
		print"solo A puede ser mayor";


def datos():
	a=int(raw_input("IngreseDatoA: "));
	b=int(raw_input("IngreseDatoB: "));
	m=suma(a,b);

def main():
	datos();
main();
raw_input(); 

