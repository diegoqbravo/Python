num=int(raw_input("ingrese numero: "));
divisores = 0;
for i in range(1,num+1):
    print i
    if(num%i==0):
        divisores=divisores+1;
if(divisores==2):
    print "el numero es primo";
else:
    print "el numero no es primo";
    
