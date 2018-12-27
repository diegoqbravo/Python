def buscarUsuario(n,a,t,c,d):
    print "\n -----BUSQUEDA USUARIOS-----";
    print "1)Buscar por Nombre";
    print "2)Buscar por Apellido";
    print "3)Volver al Menu Principal";
    opcion3=raw_input("\n seleccione una opcion: ");
    if(opcion3=="1"):
        nombre=raw_input("\n Ingrese nombre que desea buscar: ");
        if(nombre in n):
            x=n.index(nombre);            
            print "NOMBRE = ", n;
            print "APELLIDO = ", a[int(x)];
            print "1) Editar";
            print "2) Volver al menu principal";
            opcion3=raw_input("\n Seleccione su Opcion: ");
            if(opcion3=="1"):
                ####Fallo con Enteros Parte 1####
                del n[int(x)];
                del a[int(x)];
                nuevoNombre=raw_input("\n Nuevo Nombre: ");
                nuevoApellido=raw_input("\n Nuevo Apellido: ");
                n.insert(int(x), nuevoNombre);
                a.insert(int(x), nuevoApellido);
                print "NOMBRE = ", n[int(x)];
                print "APELLIDO = ", a[int(x)];
                return menu(n,a,t,c,d);
            elif(opcion3=="2"):
                return menu(n,a,t,c,d);
        else:
			print "\n Error, no existen datos Asociados"
			return menu(n,a,t,c,d);
   
    elif(opcion3=="2"):
        apellido=raw_input("\n Ingrese Apellido de Busqueda: ");
        if(apellido in a):
            x=a.index(apellido);
            print "NOMBRE = ", n[int(x)];
            print "APELLIDO = ", a;
            print "1) Editar";
            print "2) Volver al menu principal";
            opcion4=raw_input("\n Seleccione una Opcion: ");
            if(opcion4=="1"):
                ####Prueba Del####
                del n[int(x)];
                del a[int(x)];
                ##################
                nuevoNombre=raw_input("\n Nuevo Nombre: ");
                nuevoApellido=raw_input("\n Nuevo Apellido: ");
                n.insert(int(x), nuevoNombre);
                a.insert(int(x), nuevoApellido);
                print "el nuevo usuario es: ";
                print "NOMBRE=", n[int(x)];
                print "APELLIDO=", a[int(x)];
                return menu(n,a,t,c,d);
            elif(opcion4=="2"):
                return menu(n,a,t,c,d);                  
        else:
			print "\n El apellido de usuario no se Encuentra";
			return menu(n,a,t,c,d);    
    elif(opcion3=="3"):
        return menu(n,a,t,c,d);
    else:
        print "\n Error, Ingrese Sus datos Correctamente";
        buscarUsuario(n,a,t,c,d);

def ingresarUsuario(n,a,t,c,d):
    nombre=raw_input("Ingrese un Nombre: ");
    n.append(nombre);
    #################################################
    apellido=raw_input("Ingrese un Apellido: ");
    a.append(apellido);            
    #################################################
    telefono=raw_input("Ingrese un Telefono: ");
    t.append(telefono);
    #################################################
    correo=raw_input("Ingrese un Correo: ");
    c.append(correo);
    #################################################
    direccion=raw_input("Ingrese una Direccion: ");
    d.append(direccion);
    #################################################
    print "\n Datos Guardados Correctamente";
    return menu(n,a,t,c,d);

def verUsuario(n,a,t,c,d):
    ####verUsuario CON FALLAS DE VALIDACION####
    print "\n ------ USUARIO --------";
    print "1) Editar Usuario";
    print "2) Eliminar Usuario";
    print "3) Volver al menu principal";
    contador=0;
    rango=len(n);
    
    for i in range(0,rango):
        print "\n Numero de Usuario", contador," Nombre y Apellido", n[i], a[i];
        contador+=1
    opcion2=raw_input("\n Seleccione una Opcion: ");
    if(opcion2=="1"):
        seleccion=int(raw_input("\n Selecione Numero de Usuario: "));
        if(seleccion>=rango):                     
            print "Error el Usuario no Existe";                               
            return menu(n,a,t,c,d);
            
        print "Nombre = ", n[int(seleccion)];
        print "Apellido = ", a[int(seleccion)];
        ####DEL SIN PROBLEMAS####
        del n[int(seleccion)];
        del a[int(seleccion)];
        #########################
        newName=raw_input("\n Nuevo Nombre: ");
        newApellido=raw_input("\n Nuevo Apellido: ");
        n.insert(int(seleccion), newName);
        a.insert(int(seleccion), newApellido);
        print "Usuario Modificado";
        print "Nombre = ", nombre[int(seleccion)];
        print "Apellido = ", apellido[int(seleccion)];
        return menu(n,a,t,c,d);
        
    elif(opcion2=="2"):
        seleccion2=int(raw_input("\n Seleccione Numero de Usuario: "));
        print "Nombre = ", n[int(seleccion2)];
        print "Apellido = ", a[int(seleccion2)];
        seguro=raw_input("\n Seguro que Desea Eliminar S/N? ");
        
        if((seguro=="s")or(seguro=="S")):
            
            nombre=n[int(seleccion2)];
            apellido=a[int(seleccion2)];
            a.remove(apellido);
            n.remove(nombre);
            print n;
            print a;
        elif((seguro=="N")or(seguro=="n")):
            return menu(n,a,t,c,d);
        else:
            print "Error, S/N Son sus Opciones validas";
            verUsuario(n,a,t,c,d);
    elif(opcion2=="3"):
        return menu(n,a,t,c,d);
    else:
        print "Error, Seleccione una Opcion valida"
        verUsuario(n,a,t,c,d); 
 
def menu(n,a,t,c,d):
    print "---------- AGENDA ----------";
    print "1) Ingresar Usuario";
    print "2) Ver Usuario";
    print "3) Buscar Usuario";
    print "4) Salir";
    print "----------------------------";
    
    opcion=raw_input("\n Ingrese su Opcion: ");
    if(opcion=="1"):
        ingresarUsuario(n,a,t,c,d);
    elif(opcion=="2"):
        verUsuario(n,a,t,c,d);
    elif(opcion=="3"):
        buscarUsuario(n,a,t,c,d);
    elif(opcion=="4"):
        exit("\n Hasta Luego! ");
    else:
        print "\n Error, Ingrese una Opcion Valida";
        return menu(n,a,t,c,d);
n=[];
a=[];
t=[];
c=[];
d=[];
menu(n,a,t,c,d);
