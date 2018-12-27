a=int(raw_input("ingrese primer numero: "));
b=int(raw_input("ingrese segundo numero: "));
inicio=0;
if(a<b):
    for i in range(a,b+1):
        inicio+=i;
        print inicio;
else:
    print "el primero debe ser menor al segundo"
