def menu(nombre,apellido,telefono,correo,direccion):
    print "*"*8, " AGENDA ", "*"*8;
    print "1) Ingresar Usuario";
    print "2) Ver Usuario";
    print "3) Buscar Usuario";
    print "4) Salir";
    print "*"*26;
    a=raw_input("Seleccione una opcion: ");
    if(a=="1"):
        ingresar(nombre,apellido,telefono,correo,direccion);
    elif(a=="2"):
        ver(nombre,apellido,telefono,correo,direccion);
    elif(a=="3"):
        buscar(nombre,apellido,telefono,correo,direccion);
    elif(a=="4"):
        exit;
    else:
        print "seleccione una opcion valida";
        menu(nombre,apellido,telefono,correo,direccion);
def ingresar(nombre,apellido,telefono,correo,direccion):
    nom=raw_input("ingrese nombre: ");
    nombre.append(nom);
    ape=raw_input("ingrese apellido: ");
    apellido.append(ape);

              
    #tel=raw_input("ingrese telefono: ");
    #telefono.append(tel);
    #cor=raw_input("ingrese telefono: ");
    #correo.append(cor);
    #dire=raw_input("ingrese direccion: ");
    #direccion.append(dire);
    print "usuario ingresado satisfactoriamente";
    menu(nombre,apellido,telefono,correo,direccion);
def ver(nombre,apellido,telefono,correo,direccion):
    print "*"*9, " USUARIO ", "*"*9;
    print "1) Editar Usuario";
    print "2) Eliminar Usuario";
    print "3) Volver al menu principal";
    inx=0;
    ran=len(nombre);
    ran2=ran
    for i in range(0,ran):
        print "Usuario ", inx, nombre[i], apellido[i];
        inx+=1
    a=raw_input("seleccione opcion: ");
    if(a=="1"):
        b=int(raw_input("ahora seleccione usuario: "));
        while(b>=ran2):                     
            print "el usuario que selecciona no existe en la lista";                               
            menu(nombre,apellido,telefono,correo,direccion);
        print "nombre=", nombre[int(b)];
        print "apellido=", apellido[int(b)];
        del nombre[int(b)];
        del apellido[int(b)];
        d=raw_input("ingrese nuevo nombre: ");
        e=raw_input("ingrese nuevo apellido: ");
        nombre.insert(int(b), d);
        apellido.insert(int(b), e);
        print "el nuevo usuario es: ";
        print "NOMBRE=", nombre[int(b)];
        print "APELLIDO=", apellido[int(b)];
        menu(nombre,apellido,telefono,correo,direccion);
    elif(a=="2"):
        b=int(raw_input("ahora seleccione usuario: "));
        print "nombre=", nombre[int(b)];
        print "apellido=", apellido[int(b)];
        c=raw_input("esta seguro que desea eliminar este usuario? S/N ");
        if((c=="s")or(c=="S")):
            nom=nombre[int(b)];
            ape=apellido[int(b)];
            nombre.remove(nom);
            apellido.remove(ape);
            print nombre;
            print apellido;
        elif((c=="N")or(c=="n")):
            menu(nombre,apellido,telefono,correo,direccion);
        else:
            print "seleccione S/N solamente";
            ver(nombre,apellido,telefono,correo,direccion);
    elif(a=="3"):
        menu(nombre,apellido,telefono,correo,direccion);
    else:
        print "seleccione una opcion valida"
        ver(nombre,apellido,telefono,correo,direccion);
def buscar(nombre,apellido,telefono,correo,direccion):
    print "*"*4, " BUSQUEDA USUARIOS ", "*"*4;
    print "1)Buscar por nombre";
    print "2)Buscar por apellido";
    print "3)Volver al menu principal";
    a=raw_input("seleccione una opcion: ");
    if(a=="1"):
        nom=raw_input("Ingrese nombre que desea buscar: ");
        while(nom in nombre):
            b=nombre.index(nom);            
            print "NOMBRE=", nom;
            print "APELLIDO=", apellido[int(b)];
            print "1) Editar";
            print "2) Volver al menu principal";
            c=raw_input("seleccione opcion: ");
            if(c=="2"):
                menu(nombre,apellido,telefono,correo,direccion);
            elif(c=="1"):
                del nombre[int(b)];
                del apellido[int(b)];
                d=raw_input("ingrese nuevo nombre: ");
                e=raw_input("ingrese nuevo apellido: ");
                nombre.insert(int(b), d);
                apellido.insert(int(b), d);
                print "el nuevo usuario es: ";
                print "NOMBRE=", nombre[int(b)];
                print "APELLIDO=", apellido[int(b)];
                menu(nombre,apellido,telefono,correo,direccion);              
        print "El nombre de usuario no se encuentra ingresado";
        menu(nombre,apellido,telefono,correo,direccion);
    elif(a=="2"):
        ape=raw_input("Ingrese apellido que desea buscar: ");
        while(ape in apellido):
            b=apellido.index(ape);
            print "NOMBRE=", nombre[int(b)];
            print "APELLIDO=", ape;
            print "1) Editar";
            print "2) Volver al menu principal";
            c=raw_input("seleccione opcion: ");
            if(c=="2"):
                menu(nombre,apellido,telefono,correo,direccion);
            elif(c=="1"):
                del nombre[int(b)];
                del apellido[int(b)];
                d=raw_input("ingrese nuevo nombre: ");
                e=raw_input("ingrese nuevo apellido: ");
                nombre.insert(int(b), d);
                apellido.insert(int(b), d);
                print "el nuevo usuario es: ";
                print "NOMBRE=", nombre[int(b)];
                print "APELLIDO=", apellido[int(b)];
                menu(nombre,apellido,telefono,correo,direccion);              
        print "El apellido de usuario no se encuentra ingresado";
        menu(nombre,apellido,telefono,correo,direccion);    
    elif(a==3):
        menu(nombre,apellido,telefono,correo,direccion);
    else:
        print "seleccione una opcion valida";
        buscar(nombre,apellido,telefono,correo,direccion);
            











##############################################################################
nombre=[];                                                                   #
apellido=[];                                                                 #
telefono=[];                                                                 #
correo=[];                                                                   #
direccion=[];                                                                #
menu(nombre,apellido,telefono,correo,direccion);                             #
##############################################################################
