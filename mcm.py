print "calcular MCM y MCD entre 2 numeros"
num1 = int(raw_input("ingrese primer numero: "))
num2 = int(raw_input("ingrese segundo numero: "))
menor = min(num1,num2)
for i in range(1,menor):
        if (num1%i==0 and num2%i==0):
                mcd = i
                mcm = num1*num2/mcd ;
        	print "El MCM es: ", mcm ;
t=input();
