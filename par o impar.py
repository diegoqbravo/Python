def par(a):
    if a%2==0:
        print "el numero es par";
    else:
        print "el numero es impar";
def imprimir():
    a=int(raw_input("ingrese numero: "));
    poi=par(a);
    print poi;

def main():
    imprimir();


main();

