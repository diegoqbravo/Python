a=int(raw_input("ingrese primer numero: "));
b=int(raw_input("ingrese segundo numero: "));
if(a<b):
    for i in range(a,b+1):
        if(i%2==0):
            print i;
else:
    print "el primero debe ser menor al segundo"
