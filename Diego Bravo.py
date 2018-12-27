def menu(dinero,debito):
	print"\n*************** VENTAS PEAJE LOS LAGOS S.A *************";
	print"\n Recuerde que debe diferenciar los Tipos de Vehiculo";
	print"1) Categoria A";
	print"2) Categoria B";
	print"3) Categoria C";
	print"4) Categoria D";
	print"5) Chequear Categorias";
	print"6) Terminar Turno";
	print"\n*********************************************************"
	opcion=raw_input("\n Ingrese la Categoria del Vehiculo: ");
	if (opcion=="1"):
		formaPagoA(dinero,debito);
	elif (opcion=="2"):
		formaPagoB(dinero,debito);
	elif (opcion=="3"):
		formaPagoC(dinero,debito);
	elif (opcion=="4"):
		formaPagoD(dinero,debito);
	elif (opcion=="5"):
		tiposdeVehiculos(dinero,debito);
	elif (opcion=="6"):
		print"Dinero Obtenido Durante el Turno"
		print"Efectivo ", dinero
		print"Debito ", debito
	else:
		print"Error Solo tiene 6 Opciones"
		return menu(dinero,debito)
def formaPagoA(dinero,debito):
	print"Valor de la Tarifa $600";
	print"Forma de Pago?"
	print"1) Efectivo"
	print"2) Tarjeta"
	opcion2=raw_input("Ingrese su Opcion: ")
	if(opcion2=="1"):
		dinero=600+dinero
		print "\n Dinero Guardado"
		return menu(dinero,debito)
	elif(opcion2=="2"):
		debito=600+debito
		print"\n Dinero Guardado"
		return menu(dinero,debito)
	else:
		print"Solo son 2 Opciones reintente"
		return formaPagoA(dinero,debito)
def formaPagoB(dinero,debito):
	print"Valor de la Tarifa $1100";
	print"Forma de Pago?"
	print"1) Efectivo"
	print"2) Tarjeta"
	opcion3=raw_input("Ingrese su Opcion: ")
	if(opcion3=="1"):
		dinero=1100+dinero
		print "\n Dinero Guardado"
		return menu(dinero,debito)
	elif(opcion3=="2"):
		debito=1100+debito
		print"\n Dinero Guardado"
		return menu(dinero,debito)
	else:
		print"Solo son 2 Opciones reintente"
		return formaPagoB(dinero,debito)
def formaPagoC(dinero,debito):
	print"Valor de la Tarifa $1900";
	print"Forma de Pago?"
	print"1) Efectivo"
	print"2) Tarjeta"
	opcion4=raw_input("Ingrese su Opcion: ")
	if(opcion4=="1"):
		dinero=1900+dinero
		print "\n Dinero Guardado"
		return menu(dinero,debito)
	elif(opcion4=="2"):
		debito=1900+debito
		print"\n Dinero Guardado"
		return menu(dinero,debito)
	else:
		print"Solo son 2 Opciones reintente"
		return formaPagoC(dinero,debito)
def formaPagoD(dinero,debito):
	print"Valor de la Tarifa $200";
	print"Forma de Pago?"
	print"1) Efectivo"
	print"2) Tarjeta"
	opcion5=raw_input("Ingrese su Opcion: ")
	if(opcion5=="1"):
		dinero=200+dinero
		print "\n Dinero Guardado"
		return menu(dinero,debito)
	elif(opcion5=="2"):
		debito=200+debito
		print"\n Dinero Guardado"
		return menu(dinero,debito)
	else:
		print"Solo son 2 Opciones reintente"
		return formaPagoD(dinero,debito)
def tiposdeVehiculos(dinero,debito):
	print"\nTipos Categoria A";
	print"Autos, Camionetas y Station Wagons; Autos, Camionetas y Station Wagon"; 
	print"con uno o más ejes adicionales";
	print"\nTipos Categoria B";
	print"Camiones y Buses de dos ejes, Maquinaria Agrícola, de Construcción y"; 
	print"Camionetas doble rueda trasera";
	print"\nTipos Categoria C";
	print"Camiones y Buses de más de dos ejes.";
	print"\nTipos Categoria D";
	print "Motos";
	return menu();
	
dinero=0
debito=0
menu(dinero,debito);
