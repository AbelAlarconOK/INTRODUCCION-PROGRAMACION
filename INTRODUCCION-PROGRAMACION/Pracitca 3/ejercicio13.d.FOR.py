#d) Idem anterior para la sucesión an =1/n**2.

n=int(input("ingrese un numero positivo: "))

suma=0
for i in range(1,n+1):
    print("1/",i,"denom: ",i**2)
    suma=suma+(1/i**2)
    print(suma)