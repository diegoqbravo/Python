n[];
a[];
menu(n,a);
def menu():
	print "********* AGENDA **********"
	print "1) Ingresar Usuario"
	print "2) Ver Usuario"
	print "3) Buscar Usuario"
	print "4) Salir"
	print "***************************"
	opcion=raw_input("\n Ingrese Opcion: ")
	if(opcion == "1"):
		ingresarUsuario();
	elif(opcion == "2"):
		verUsuario();
	elif(opcion == "3"):
		buscarUsuario();
	elif(opcion == "4")
		exit("\n Hasta Luego");
def ingresarUsuario():
	nombre=raw_input("Ingrese Nombre: ")
	n.insert[0,nombre]
	apellido=raw_input("Ingrese Apellido: ")
	a.insert[0,apellido]
	telefono=raw_input("ingrese Telefono: ")
	correo=raw_input("Ingrese Correo: ")
	direccion=raw_input("Ingrese Direccion: ")
	
