n=[];
a=[];
t=[];
c=[];
d=[];
menu(n,a,t,c,d);
def menu(n,a,t,c,d):
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
	elif(opcion == "4"):
		exit("\n Hasta Luego");
def ingresarUsuario(n,a,t,c,d):
	nombre=raw_input("Ingrese Nombre: ")
	n.insert[0,nombre]
	apellido=raw_input("Ingrese Apellido: ")
	a.insert[0,apellido]
	telefono=raw_input("ingrese Telefono: ")
	t.insert[0,telefono]
	correo=raw_input("Ingrese Correo: ")
	c.insert[0,correo]
	direccion=raw_input("Ingrese Direccion: ")
	d.insert[0,direccion]
	return menu(n,a,t,c,d);
def verUsuario(n,a,t,c,d):
	print"\n 1) Editar Usuario";
	print"2) Eliminar Usuario";
	print"3) Volver al Menu Principal";
	opcion2=raw_input("\n Ingrese su Opcion: ")
	if(opcion2== "1"):
		nuevoUsuario=raw_input("\n Ingrese su Nuevo Nombre: ")
		n.index[2,nuevoUsuario]
		nuevoApellido=raw_input("\n Ingrese su Nuevo Apellido: ")
		a.index[2,nuevoApellido]
		nuevoTelefono=raw_input("\n Ingrese su Nuevo Telefono: ")
		t.index[2,nuevoTelefono]
		nuevoCorreo=raw_input("\n Ingrese su Nuevo Correo: ")
		c.index[2,nuevoCorreo]
		nuevoDireccion=raw_input("\n Ingrese su Nueva Direccion: ")
		d.index[2,nuevoDireccion]
		return menu(n,a,t,c,d);
	elif(opcion2=="2"):
		print"HOLA"
	elif(opcion2 =="3"):
		print"HOLA"
		return menu();
