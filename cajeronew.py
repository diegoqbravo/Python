"cajero"
i=      0;
cont=5;
def user(i):
	a=raw_input("Ingrese Usuario: ");
	if (a=="elProfe"):
		print "Correcto";
		b=raw_input("Ingrese Clave: ");
		if (b=="1"):
			print "Correcto"
			menu(i);
		else:
			cont+=(-1);
			if cont==0:
				print "Hasta luego, vuelve cuando sepas los datos!"
			exit(i);
	else:
		print "Datos incorrectos, vuelva a intentar"
		user(i);
	
print               "CAJERO AUTOMATICO";
def menu(i):
	print "      ****************************";
	print "      * 1- Depositar Dinero      *";
	print "      * 2- Retirar Dinero        *";
	print "      * 3- Transferir Dinero     *";
	print "      * 4- Ver Dinero Disponible *";
	print "      * 5- Ingresar Dinero       *";
	print "      ****************************";
	h=raw_input("      *Ingrese Su Opcion: ");

	if (h=="1"):
		depo(i);
	if (h=="2"):
		retiro(i);
	if (h=="3"):
		trans(i);
	if (h=="4"):
		dispo(i);
	if (h=="5"):
		ingre(i);
	else:
		menu(i);
def depo(i):
	remi=raw_input("Ingrese Destinatario a Depositar: ");
	if len(remi)==12:
		f=int(raw_input("Ingrese Dinero a Depositar: "));
		print "El Dinero Fue depositado";
	
def retiro(i):
	re=raw_input("Cuanto Dinero Desea Retirar: ");
	if (re<=i):
		i=i-re;
		print "Retire Su Dinero";
	else:
		print "El Dinero Solicitado NO Es Suficiente";
		
def trans(i):	
	cu=raw_input("Cuenta de Destino: ");
	de=raw_input("Nombre de Destino: ");
	co=raw_input("Correo Electronico: ");
	ba=raw_input("Banco Del Destinatario: ");
	mo=raw_input("Monto A Transferir: ");
	if (mo<=i*89/100):
		print "El Dinero Fue TRansferido Correctamente";
		
	else:
		print "El Monto Ingresado Es Menor O Superior A Lo Permitido";
		
def dispo(i):
	print i;
	
def ingre(i):
	z=int(raw_input("Cuanto Dinero Desea Ingresar: "));
	if (z>=100000) and (z<=99999999):
		print "Su Dinero Fue Depositado Satisfactoriamente";
		i=i+z;
		menu(i);
	else:
		print "El Monto Ingresado No Es Valido";
		
		
user(i);
