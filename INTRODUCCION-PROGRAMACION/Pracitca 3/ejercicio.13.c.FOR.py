#c) Idem anterior para la sucesión an = n3 − n2.

n=int(input("ingrese un numero positivo: "))

suma=0
for i in range(1,n+1):
    suma=suma+((i*3)-(i*2))
    print(suma)
