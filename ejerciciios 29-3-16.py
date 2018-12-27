def SumaNum(a,s,d,f,g):
    Suma=a+s+d+f+g;
    return Suma;

def Resta(a,s,d,f,g):
    res=a-s-d-f-g;
    return res;

def Div(a,b):
    if b!=0:
        divi=a/b;
        return divi;
    else:
        return "la division por cero no es posible, validar eso";

def RestoDiv(a,b):
    if b!=0:
        resto=a%b;
        return resto;

def posneg(a):
    if a>0:
        print "el numero es positivo";
    elif a<0:
        print "el numero es negativo";
    else:
        print "el numero es 0";

def comparacion(a,b):
    if a==b:
        print "ambos numeros tienen igual valor";
    elif a > b:
        print "el primer numero es mayor que el segundo";
    else:
        print "el segundo numero es mayor que el primero";

def menor(a,b,c):
    if ((a<b)and(a<c)):
        print "el primer numero es el menor de los tres";
    elif ((b<a)and(b<c)):
        print "el segundo numero es el menor de los tres";
    elif ((a==b)and(b==c)):
        print "los tres numeros son iguales";
    else:
        print "el tercer numero es el menor de los tres";

def IMC(a,b):
    if b!=0:
        iemece=(a//(b*b))
        return iemece;
    else:
        print "ingrese valores validos";

def par(a):
    if (a%2==0):
        print "el numero es par"
    else:
        print "el numero es impar"

def imp1():
    a=int(raw_input("ingrese primer numero: "));
    s=int(raw_input("ingrese segundo numero: "));
    d=int(raw_input("ingrese tercer numero: "));
    f=int(raw_input("ingrese cuarto numero: "));
    g=int(raw_input("ingrese quinto numero: "));
    im=SumaNum(a,s,d,f,g);
    print im;

def main1():
    imp1();

def imp2():
    a=int(raw_input("ingrese primer numero: "));
    s=int(raw_input("ingrese segundo numero: "));
    d=int(raw_input("ingrese tercer numero: "));
    f=int(raw_input("ingrese cuarto numero: "));
    g=int(raw_input("ingrese quinto numero: "));
    im2=Resta(a,s,d,f,g);
    print im2;

def main2():
    imp2();

def imp3():
    a=int(raw_input("ingrese numero que va a dividir: "));
    b=int(raw_input("ingrese por que numero lo va a dividir: "));
    im3=Div(a,b);
    print im3;

def main3():
    imp3();

def imp4():
    a=int(raw_input("ingrese numero: "));
    im4=posneg(a);
    print im4;
def main4():
    imp4();
    
def imp5():
    a=int(raw_input("ingrese primer numero: "))
    b=int(raw_input("ingrese segundo numero: "))
    im5=comparacion(a,b);
    print im5;
def main5():
    imp5();

def imp6():
    a=int(raw_input("ingrese el primer numero: "));
    b=int(raw_input("ingrese el segundo numero: "));
    c=int(raw_input("ingrese el tercer numero: "));
    im6=menor(a,b,c);
    print im6;
def main6():
    imp6();
def imp7():
    a=int(raw_input("ingrese peso: "));
    b=int(raw_input("ingrese estatura: "));
    im7=IMC(a,b);
    print im7;
def main7():
    imp7();
def imp9():
    a=int(raw_input("ingrese numero: "));
    im9=par(a);
    print im9;
def main9():
    imp9();

#ejercicio 1#
print "suma de 5 numeros"
main1();

#ejercicio 2#
print "resta de 5 numeros"
main2();

#ejercicio 3#
print "division:"
main3();

#ejercicio 4#
print "numero positivo o negativo"
main4();

#ejercicio 5#
print "comparacion de valores"
main5();

#ejercicio 6#
print "menor entre tres numeros"
main6();

#ejercicio 7#
print "calcular IMC"
main7();

#ejercicio 8#
print "det. si el numero es primo"

#ejercicio 9#
print "numero par o impar"
main9();
