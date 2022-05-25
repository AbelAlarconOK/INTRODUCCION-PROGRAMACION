#Realizar un programa que sume los primeros números impares hasta n.
# (n lo indica el usuario) 1+3+5+…+n=
n=int(input("ingrese numero impar: "))
i=1
suma=0
while (i<=n):
    suma=suma+i
    i=i+2
print(suma)
