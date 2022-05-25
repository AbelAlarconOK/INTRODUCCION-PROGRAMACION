#d) Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla la suma de los divisores de n.

n=int(input("ingrese un numero positivo: "))
i=1
suma_div=0
while i<=n:
    if n%i==0:
        suma_div=suma_div+i
    i=i+1
print("la suma de los divisores de", n, "es: ",suma_div)
