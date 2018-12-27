def soluecu(a,b):
    x=-b/a;
    return x;

def imprimir():
    print "ingrese valor de a: ";
    a=input();
    print "ingrese valor de b: ";
    b=input();
    if a==0:
        print "la ecuacion no tiene solucion al tener mas de una imagen en el eje Y";
    else:
        print "la solucion de la ecuacion es: ",  soluecu(a,b);
def main():
    imprimir();
print "los factores de una ecuacion estan en la forma (ax+b=0)"
main();
raw_input();



        
