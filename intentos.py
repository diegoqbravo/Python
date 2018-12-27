intentos = 0;
contador = 5;
usuario = "elProfe";
clave = "1";

while(intentos < contador):
	ingresoUsuario = raw_input('Ingrese Usuario: ');
	ingresoClave = raw_input('Ingrese Clave: ');
	if(ingresoUsuario == usuario and ingresoClave == clave):
		menu();
		break;
	else:
		print 'Datos incorrectos, vuelva a intentar';
		intentos+=1;
	if(intentos == contador):
		print "\n  Hasta luego, vuelve cuando sepas los datos";
