a=int(raw_input("ingrese numero: "));
inicio=1;
if(0<a):
    for i in range(1,a+1):
        inicio*=i;
        print inicio;
else:
    print "el numero debe ser positivo"
