#Realizar un programa que sume los primeros n números impares.(n lo indica el usuario)
#	Ejemplo: para n=7  debe dar el resultado de 	1+3+5+7+9+11+13

n=int(input("ingrese numero impar: "))
i=11
suma=0
while (i<=n):
    suma=suma+i
    print(i,suma)
    i=i+2
print(n,"=",suma)

#termianar de resolver.