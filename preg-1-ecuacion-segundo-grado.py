def soluecu(a,b,c):    
    z=(b*b-4*a*c);    
    if z>=0:
        x=(-b+(b*b-4*a*c)**(0.5))/(2*a);
        xd=(-b-(b*b-4*a*c)**(0.5))/(2*a);        
        if ((x!=xd)and(xd!=x)):
            print "las soluciones de la ecuacion son: ",(x ,0), (xd,0);
        else:
            print "la solucion de la ecuacion es: ",(x ,0);
    else:
        print "la parabola de dicha ecuacion nunca corta al eje de las x";
        print "por ende, no tiene solucion";

def ingresar():
    a=input();
    print "ingrese valor de b: ";
    b=input();
    print "ingrese valor de c: ";
    c=input();
    soluecu(a,b,c);
print "calcular las soluciones de una ecuacion de segundo grado";
print "los factores en la ecuacion estan en la forma (ax^2+bx+c=0)";
print "ingrese valor de a: ";
ingresar();
raw_input();




