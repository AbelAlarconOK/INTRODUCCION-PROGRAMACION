#c) Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla la cantidad de divisores de n.

n=int(input("ingrese un numero positivio: "))
i=1
div=0
while (i<=n):
    if n%i==0:
        div=div+1
    i=i+1
print("cantidad de divisores de ",n, "son: ", div)



