def menu(d):
	print"Opcion 1 Depositar Dinero";
	print"Opcion 2 Retirar Dinero";
	print"Opcion 3 Tranferir Dinero";
	print"Opcion 4 Saldo Disponible";
	print"Opcion 5 Ingresar Dinero";
	print"Opcion 6 Salir"
	opcion=raw_input("Ingrese su Opcion: ");
	if (opcion=="1"):
		deposito(d);
	elif (opcion=="2"):
		retiro(d);
	elif (opcion=="3"):
		transferencia(d);
	elif (opcion=="4"):
		saldo(d);
	elif (opcion=="5"):
		ingreso(d);
	elif (opcion=="6"):
		exit("ADIOS!");
	else:
		print "Error"
		print "Recuerda que solo son 5 Opciones"
		return menu(d);
def deposito(d):
	destinatario=raw_input("Nombre de Cuenta: ");
	if len(destinatario)==12:
		f=int(raw_input("Cuanto Dinero Desea Depositar?: "));
		if(f<=d):
			print f, "Fueron Depositados";
			print "Tu Saldo Actual es de ", d-f;
			d=d-f
			return menu(d);
		else:
			print "no tienes dinero para depositar";
			return menu(d);
	else:
		print"El Nombre de Cuenta esta Incorrecto, deben ser 12 Caracteres con Letras";
		return menu(d);	
def retiro(d):
	retirar=int(raw_input("Cuanto Dinero Desea Retirar: "));
	if (retirar<=d):
		d=d-retirar;
		print d, "Fueron Retirados";
		return menu(d);
	else:
		print "No tienes suficiente dinero para Retirar";
		return menu(d);
		
def transferencia(d):	
	cuenta=raw_input("Cuenta de Destino: ");
	destino=raw_input("Nombre de Destino: ");
	correo=raw_input("Correo Electronico: ");
	banco=raw_input("Banco Del Destinatario: ");
	monto=int(raw_input("Monto A Transferir: "));
	if (monto<=d*89/100):
		print "El Dinero Fue Transferido Correctamente";
		print "Tu Saldo Actual es de ", d-monto;
		return menu(d);
	else:
		print "El Monto Ingresado Es Menor O Superior A Lo Permitido";
		return menu(d);
		
def saldo(d):
	print "Tienes", d ,"de Saldo disponible";
	return menu(d);
	
def ingreso(d):
	c=int(raw_input("Cuanto Dinero Desea Ingresar: "));
	if (c>=100000) and (c<=9999999):
		print "Su Dinero ha sido Ingresado Correctamente";
		d=d+c;
		print "Su Saldo Actual es de", d;
		return menu(d);
	else:
		print "El Monto Ingresado No Es Valido, debe ser mayor a 100.000 y menor a 9.999.999";
		print "Vuelve a intentarlo";
		return menu(d);
def usuario(d,contador,intentos):
	usuario = "elProfe";
	clave = "1";
	while(intentos < contador):
		ingresoUsuario = raw_input('Ingrese Usuario: ');
		ingresoClave = raw_input('Ingrese Clave: ');
		if(ingresoUsuario == usuario and ingresoClave == clave):
			return menu(d);
			break;
		else:
			print 'Datos incorrectos, vuelva a intentar';
			intentos+=1;
		if(intentos == contador):
			print "\n  Hasta luego, vuelve cuando sepas los datos";	
intentos = 0;
contador = 5;
d= 100000;
usuario(d,contador,intentos);
