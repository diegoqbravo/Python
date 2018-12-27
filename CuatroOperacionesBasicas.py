import cuatrobasicas;
import menu;
MN=menu;
s=MN.menu();
cb=cuatrobasicas;
variableQueSoloExisteAca=cb.bienvenido();
print variableQueSoloExisteAca;
m=raw_input("Ingrese Su Opcion: ");

if (m=="1"):
	print "Usted Esta En Operacion SUMA";
	numUno=int(raw_input("Ingrese Numero Uno"));
	numDos=int(raw_input("Ingrese Numero Dos"));
	suma=cb.funcionQueSuma(numUno,numDos);
	print "El Resultado Es", suma;
	MN.menu();
	
elif (m=="2"):
	print "Usted Esta En Operacion RESTA";
	numUno=int(raw_input("Ingrese Numero Uno"));
	numDos=int(raw_input("Ingrese Numero Dos"));
	resta=cb.funcionQueResta(numUno,numDos);
	print "El Resultado Es", resta;
	s=MN.menu();

elif (m=="3"):
	print "Usted Esta En Operacion MULTIPLICACION";
	numUno=int(raw_input("Ingrese Numero Uno"));
	numDos=int(raw_input("Ingrese Numero Dos"));
	multi=cb.funcionQuemulti(numUno,numDos);
	print "El Resultado Es", multi;
	s=MN.menu();

elif (m=="4"):
	print "Usted Esta En Operacion DIVISION";
	numUno=int(raw_input("Ingrese Numero Uno"));
	numDos=int(raw_input("Ingrese Numero Dos"));
	if(numDos==0):
		print "No Se Pueden Realizar Divisiones Por 0";
		exit;
	else:
		divi=cb.funcionQuedivi(numUno,numDos);
		print "El Resultado Es", divi;
	s=MN.menu();
	
	
