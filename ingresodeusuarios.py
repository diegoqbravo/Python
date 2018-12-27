attempts = 0;
retry = 5;
user = 'Diego';
password = 'DiegoMascala';

while(attempts < retry):
	input_user = raw_input('Ingrese Usuario: ');
	input_psswd = raw_input('Ingrese Clave: ');

	if(input_user == user and input_psswd == password):
		menu();
		break;
	else:
		print 'Datos incorrectos, vuelva a intentar';
		attempts+=1;
if(attempts == retry):
	print '\n  Hasta luego, vuelve cuando sepas los datos';
else:
	print '\n  Hasta luego, {0}'.format(input_user);
