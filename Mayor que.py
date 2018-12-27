#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Mayor que.py

def validacionM(a,b):
	if(a>b):
		print("A es Mayor que B");
	elif(a==b):
		print("A y B son Iguales")
	else:
		print("B es Mayor que A");
def imprimir():
	a=int(raw_input("Ingrese A Numero: "));
	b=int(raw_input("Ingrese B Numero: "));
	c=validacionM(a,b);
def main():
	imprimir();
main();	

