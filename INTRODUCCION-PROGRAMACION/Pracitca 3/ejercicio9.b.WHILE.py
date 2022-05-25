#b) Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla todos los divisores pares de n.

n=int(input("ingrese un numero positivo: "))
i=2
while i<=n:
    if (n%i)==0:
        print(i)
    i=i+2

