#d) Idem anterior para la sucesión an =1/n**2.

n=int(input("ingrese ùn numero positivo: "))

i=1
suma=0
while i <=n:
    print("1/",i,"denom:",i**2)
    suma=suma+(1/i**2)
    i=i+1
    print(suma)
