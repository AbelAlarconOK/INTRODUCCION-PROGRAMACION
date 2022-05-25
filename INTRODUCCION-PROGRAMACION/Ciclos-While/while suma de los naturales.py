#Realizar un programa que sume los primeros n nÃºmeros naturales.
# (n lo indica el usuario) 1+2+3+4+â€¦+n =

n=int(input("ingrese un numero: "))
i=1
suma=0
while(i<=n):
    suma=suma+i
    print(i,suma)
    i=i+1
print(suma)

