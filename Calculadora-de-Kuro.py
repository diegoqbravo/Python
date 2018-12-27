print "*********calculadora de Kuro*********";
print "  "
print "para que funcione debe escoger una funcion o formula"
print "la forma de interaccion es>>> Numero+enter"
print "es importante que se use el . en los digitos, (el uso de la ',' causa la destruccion del mundo)"
print " "
print "(0) para cerrar"
print "(1) Sumar 2 numeros"
print "(1.5) Suma de angulos interiores segun cantidad de lados"
print "(2) multiplicar 2 numeros"
print "(3) dividir 2 numeros"
print "(4) restar 2 numeros"
print "(4.5) potencia"
print "(4.6) raiz cuadrada"
print "(5) Area triangulo"
print "(5.5)Volumen piramide base 4 lados"
print "(5.6) Volumen Cono"
print "(5.7) Area Cono"
print "(6) perimetro triangulo"
print "(7) A,P Cuadrado+ Vol Cubo"
print "(8) area y perimetro rectangulo"
print "(9) Area rombo"
print "(9.5) perimetro rombo"
print "(10) Area y perimetro romboide"
print "(11) Area trapecio"
print "(11.5) Perimetro trapecio"
print "(12) area circulo"
print "(13) perimetro circunferencia"
print "(14) volumen esfera"
print "(14.4) Area tetraedro"
print "(14.5) Area octaedro"
print "(14.6) Area icosaedro"
print "(15) seno del angulo"
print "(16) Coseno del angulo"
print "(17) tangente del angulo"
print "(18) cosec del angulo"
print "(19) Sec del angulo"
print "(20) cotang del angulo"
print "(21) Raices parabola"
print "(22) coordenadas vertice parabola"
print "(23) calcular porcentaje"
print "(24) Calcular cantidad del porcentaje"
print "(25) calcular el 100%"
print "(26) Hip. con Teo.Pitagoras"
print "(26.5) cat. con Teo.Pitagoras"
print "(27) Factorial"
print "(28) MCM y MCD entre 2 numeros"
		
import math
print "seleccione una opcion para operar"
a=input();
while a!=0:
        if a==1: 
                print "Sumar dos numeros"
                print "primer numero"
                b=input()
                print "segundo numero"
                c=input()
                print "resultado es: ", b+c;
        elif a==1.5:
                print "suma de angulos interiores de una figura geometrica segun cantidad de lados"
                print "cantidad de lados de la figura:"
                b=input()
                print "la suma de los antulos interiores de la figura= ", 180*(b-2);
        elif a==2:
                print "multiplicacion de dos numeros"
                print "primer numero"
                b=input()
                print "segundo numero"
                c=input()
                print "el resultado es: ", b*c;
        elif a==3:
                print "dividir dos numeros"
                print "numero que dividiremos"
                b=input()
                print "dividido por"
                c=input()
                if c==0:
                        print "La division por 0 no esta definida"
                print "el resultado es: ", b/c
                print "y da resto(modulo): ", b%c;
        elif a==4:
                print "restar dos numeros"
                print "primer numero"
                b=input()
                print "segndo numero"
                c=input()
                print "el resultado es: ", b-c;	
        elif a==4.5:
                print "potencia"
                print "numero: "
                b=input()
                print "elevado a:"
                c=input()
                print "el resultado es: ", b**c;
        elif a==4.6:
                print "Raiz cuadrada"
                print "numero: "
                b=input()
                print "la raiz cuadrada es: ", b**0.5;
        elif a==5:
                print "Area triangulo"
                print "base: "
                b=input()
                print "altura: "
                c=input()
                print "Area del triangulo es: ", b*c/2;	
        elif a==5.5:
                print "Volumen de una piramida de base de 4 lados"
                print "ancho de la base:"
                b=input()
                print "largo de la base:"
                c=input()
                print "altura de la piramide"
                d=input()
                print "volumen de la piramide es: ", b*c*d/3;
        elif a==5.6:
                print "Volumen de un cono"
                print "radio de la base:"
                r=input()
                print "altura del cono:"
                h=input()
                print "Volumen del cono es: ", 3.1415926535*r*r*h/3;
        elif a==5.7:
                print "Area de un cono"
                print "radio:"
                r=input()
                print "apotema:"
                g=input()
                print "Area del cono es: ", 3.1415926535*r*r+3.1415926535*r*g;	
        elif a==6:
                print "perimetro triangulo"
                print "primer cateto"
                b=input()
                print "segundo cateto"
                c=input()
                print "tercer cateto"
                d=input()
                print "perimetro del triangulo es: ", b+c+d;	
        elif a==7:
                print "Area y perimetro cuadrado; Volumen Cubo"
                print "lado:"
                b=input()
                c=math.sqrt(b*b+b*b)
                d=math.sqrt(b*b+c*c)
        	print "Area: ", b*b;
                print "Perimetro: ", b*4;
        	print "Volumen cubo: ", b*b*b;
                print "Diagonal del cuadrado: ", c;
        	print "Diagonal del cubo: ", d;		
        elif a==8:
                print "Area y perimetro de rectangulo"
                print "lado uno:"
                b=input()
                print "lado dos:"
                c=input()
                print "Area rectandulo: ", c*b
                print "Perimetro rectangulo: ", c+c+b+b;	
        elif a==9:
                print "Area de rombo"
                print "primera diagonal:"
                b=input()
                print "segunda diagonal:"
                c=input()
                print "Area del rombo es: ", c*b;	
        elif a==9.5:
                print "Perimetro rombo"
                print "lado:"
                b=input()
                print "Perimetro del rombo es: ",b*4;	
        elif a==10:
                print "Area y perimetro romboide"
                print "base: "
                b=input()
                print "altura"
                c=input()
                print "Area romboide es: ", c*b
                print "Perimetro romboide es: ", c+c+b+b;	
        elif a==11:
                print "Area trapecio"
                print "altura:"
                b=input()
                print "Base menor:"
                c=input()
                print "Base mayor:"
                d=input()
                print "Area del trapecio es: ", b*c*d/2;	
        elif a==11.5:
                print "Perimetro del trapecio"
                print "base menor:"
                b=input()
                print "base mayor:"
                c=input()
                print "Lado:"
                d=input()
                print "Perimetro del trapecio es: ", d+d+c+b;
        elif a==12:
                print "Area del circulo"
                print "radio:"
                b=input()
                print "area del circulo es: ", b*b*3.1415926535;
        elif a==13:
                print "Circunferencia(perimetro)"
                print "radio:"
                b=input()
                print "perimetro de la circunferencia es: ", 2*b*3.1415926535;	
        elif a==14:
                print "Volumen esfera"
                print "radio:"
                b=input()
                print "volumen de la esfera es: ", b*b*b*3.1415926535*4/3;	
        elif a==14.4:
                print "Area tetraedro(4 caras, triangulos equilateros)"
                print "valor de un lado:"
                b=input()
                print "Area del tetraedtro es: ", b*b*math.sqrt(3);
        elif a==14.5:
                print "Area Octaedro(8 caras, triangulos equilateros)"
                print "valor de un lado:"
                b=input()
                print "Area del Octaedro es: ", 2*b*math.sqrt(3);
        elif a==14.6:
                print "Area Icosaedro(20 caras, triangulos equilateros)"
                print "valor de un lado:"
                b=input()
                print "Area del icosaedro es: ", 5*b*math.sqrt(3);	
        elif a==15:
                print "Seno del angulo:"
                print "angulo: "
                n=input()
                b=n*0.0174533
                print "Sin(x)= ", math.sin(b);
        elif a==16:
                print "Coseno del angulo:"
                print "angulo:"
                n=input()
                b=n*0.0174533
                print "Cos(x)= ", math.cos(b);
        elif a==17:
                print "Tangente del angulo"
                print "angulo:"
                n=input()
                b=n*0.0174533
                print "Tan(x)= ", math.tan(b);
        elif a==18:
                print "Cosecante del angulo"
                print "angulo:"
                n=input()
                b=n*0.0174533
                print "Csc(x)= ", 1/(math.sin(b));
        elif a==19:
                print "Secante del angulo"
                print "angulo:"
                n=input()
                b=n*0.0174533
                print "Sec(x)= ", 1/(math.cos(b));
        elif a==20:
                print "cotangente del angulo"
                print "angulo:"
                n=input()
                b=n*0.0174533
                print "Tan(x)= ", 1/math.tan(b);
        elif a==21:
                print "raices de la funcion cuadratica"
                print "ax(2) +bx +c"
                print "valor de a:"
                b=input()
                print "valor de b:"
                c=input()
                print "valor de c:"
                d=input()
                print "Las raices de la funcion son: "
                print "x1= ",(-c+math.sqrt(c*c+4*b*d))/2*b 
                print "x2= ",(-c-math.sqrt(c*c+4*b*d))/2*b;
        elif a==22:
                print "Coordenadas del Vertice de una parabola"
                print "ax(2) +bx +c"
                print "valor de a:"
                b=input()
                print "valor de b:"
                c=input()
                print "valor de c:"
                d=input()
                e=(-c/(b+b))
                print "Coordenadas del vertice son: "
                print "x= ", e 
                print "y= ", b*e*e+c*e+d;
        elif a==23:
                print "Calcular porcentaje"
                print "nuestro 100% es: "
                b=input()
                print "Cantidad que se quiere obtener el %: "
                c=input()
                print "el porcentaje es:(%) ", c*100/b;
        elif a==24:
                print "Calcular cantidad del x porcentaje"
                print "nuestro 100% es:"
                b=input()
                print "nuestro x% es:"
                c=input()
                print "nuestro x%= ", c*b/100;
        elif a==25:
                print "calcular el 100%"
                print "cantidad que se tiene:"
                b=input()
                print "porcentaje al que equivale:"
                c=input()
                print "el 100%= ", b*100/c;
        elif a==26:
                print "Calcular hipotenusa con teorema de pitagoras"
                print "primer cateto:"
                b=input()
                print "segundo cateto:"
                c=input()
                d=b*b+c*c
                print "Hipotenusa= ", math.sqrt(d);
        elif a==26.5:
                print "Calcular el valor de un cateto con teorema de pitagoras"
                print "cateto conocido:"
                b=input()
                print "hipotenusa:"
                c=input()
                d=c*c-b*b
                print "valor del cateto es: ", math.sqrt(d);
        elif a==27:
                print "Factorial de X numero"	
                print "x= ?"
                b=input()
                print "Su factorial es: ", math.factorial(b);
        elif a==28:
                print "calcular MCM y MCD entre 2 numeros"
                num1 = int(raw_input("ingrese primer numero: "))
                num2 = int(raw_input("ingrese segundo numero: "))
                menor = min(num1,num2)
                for i in range(1,menor):
                	if (num1%i==0 and num2%i==0):
                		mcd = i
                		mcm = num1*num2/mcd ;
        	
        	print "El MCM es: ", mcm ;
                print "El MCD es: ", mcd ;
        elif a==7.7:
                rut = raw_input("rut sin digito verificador: ")
                suma=0
                multi= 2
                for r in rut [::-1]:
                        suma += int (r) * multi
                        multi += 1
                        if multi == 8:
                                multi = 2.
                resto = suma % 11
                resta = 11 - resto
                if resta == 11:
                        print "el digito verificador es: 0"
                elif resta == 10:
                        print "el digito verificador es: K"
                else:
                        print "el digito verificador es %d" % (resta);
                                
        print "seleccione una opcion para operar:"
        a=input()
	




			
				
			
			

		
	
