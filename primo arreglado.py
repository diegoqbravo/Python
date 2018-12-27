def primo(a):
    if ((a%2==0)and(a!=2)):
        print "el numero no es primo";
    elif ((a%3==0)and(a!=3)):
        print "el numero no es primo";
    elif ((a%5==0)and(a!=5)):
        print "el numero no es primo";
    elif ((a%7==0)and(a!=7)):
        print "el numero no es primo";
    else:
        print "el numero es primo";
    
def imp8():
    a=int(raw_input("ingrese el numero: "));
    if a==1:
        print "La definicion de numeros primos solo se aplica para numeros enteros positivos mayores a 1"
    else:
        im8=primo(a);
        return im8;
    
def main8():
    imp8();

main8();
