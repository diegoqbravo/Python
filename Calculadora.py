def depositar(dd):
    print "ingrese cuenta";
    a=raw_input();
    if(len(a)==12):
        b=int(raw_input("ingrese el monto de dinero a depositar: "));
        if b>0:
            print "ha ingresado $", b, "a la cuenta", a;
            main(dd);
        else:
            print "SI NO HAY DINERO, NO SE PUEDE DEPOSITAR";
            main(dd);
    else:
        print "ingrese numero de cuenta con 4 numeros y 8 letras";
        depositar(dd);
def retirar(dd):
    if (dd>0):
        c=int(raw_input("Cuando dinero desea retirar: "));
        if (c>0):
            dd=dd-c;
            main(dd);
        else:
            print "no puede retirar dinero negativo, esa es otra opcion";
            main(dd);
    else:
        print "no se puede retirar si no hay dinero en la cuenta";
        main(dd);
def transferir(dd):
    if (dd<=0):
        print "no puede transferir si no posee dinero";
    else:
        print "ingrese cuenta de destino";
        d=raw_input();
        print "ingrese nombre de destino";
        e=raw_input();
        print "ingrese correo electronico";
        f=raw_input();
        print "ingrese banco al que pertenece";
        g=raw_input();
        h=int(raw_input("ingrese monto de dinero que desea transferir"));
        h2=dd*89/100;
        if (h<=h2):
            print "usted ha transferido: $", h;
            print "a la cuenta de: ", e;
            print "cuenta: ", d;
            print "del banco: ", g;
            main(dd);
        else:
            print "no puede transferir tanto dinero en relacion al que dispone";
            main(dd);
def ver(dd):
    print "usted dispone de: $", dd;
    main(dd);
def ingresar(dd):
    i=int(raw_input("cuanto dinero desea ingresar en la cuenta: "));
    if ((i<=99999999)and(i>=100000)):
        dd=dd+i;
        main(dd);
    else:
        print "debe ingresar dinero entre $100.000 y $99.999.999";
        main(dd);
def main(dd):
    if(dd==0):
        print "primero debe ingresar dinero en la cuenta";
        i=int(raw_input("cuanto dinero desea ingresar en la cuenta: "));
        if ((i<=99999999)and(i>=100000)):
            dd=dd+i;
            main(dd);
        else:
            print "debe ingresar dinero entre $100.000 y $99.999.999";
            main(dd);
    print "*"*10;
    print "1- Depositar dinero";
    print "2- Retirar dinero";
    print "3- Transferir dinero";
    print "4- Ver dinero disponible";
    print "5- Ingresar dinero";
    print "*"*10;
    opc=int(raw_input("seleccione una opcion: "));
    if (opc==1):
        depositar(dd);
    elif (opc==2):
        retirar(dd);
    elif (opc==3):
        transferir(dd);
    elif (opc==4):
        ver(dd);
    elif (opc==5):
        ingresar(dd);
    else:
        print "ingrese una opcion valida";
        main(dd);
print "bienvenido";
dd=0;
print "ingrese Usuario: ";
usuario=raw_input();
print "ingrese clave";
clave=raw_input();
if ((usuario=="elProfe")and(clave=="e1L2p3R4oF5e.-.@85")):
    main(dd);
else:
    print "su usuario o contrase\xa4a no son validos";
    print "ingrese datos validos";
print "ingrese Usuario: ";
usuario=raw_input();
print "ingrese clave";
clave=raw_input();
if ((usuario=="elProfe")and(clave=="e1L2p3R4oF5e.-.@85")):
    main(dd);
else:
    print "su usuario o contrase\xa4a no son validos";
    print "ingrese datos validos";
print "ingrese Usuario: ";
usuario=raw_input();
print "ingrese clave";
clave=raw_input();
if ((usuario=="elProfe")and(clave=="e1L2p3R4oF5e.-.@85")):
    main(dd);
else:
    print "su usuario o contrase\xa4a no son validos";
    print "ingrese datos validos";
print "ingrese Usuario: ";
usuario=raw_input();
print "ingrese clave";
clave=raw_input();
if ((usuario=="elProfe")and(clave=="e1L2p3R4oF5e.-.@85")):
    main(dd);
else:
    print "su usuario o contrase\xa4a no son validos";
    print "ingrese datos validos";
print "ingrese Usuario: ";
usuario=raw_input();
print "ingrese clave";
clave=raw_input();
if ((usuario=="elProfe")and(clave=="e1L2p3R4oF5e.-.@85")):
    main(dd);
else:
    print "su usuario o contrase\xa4a no son validos";
    print "Hasta luego, vuelve cuando sepas los datos!";

    
        
    
