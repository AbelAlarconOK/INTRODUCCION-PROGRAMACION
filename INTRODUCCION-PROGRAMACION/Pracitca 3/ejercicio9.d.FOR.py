#d) Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla la suma de los divisores de n.

n=int(input("ingrese un numero positivo: "))
suma_divi=0
for i in range(1,n+1):
    if n%i==0:
        suma_divi=suma_divi+i
print("la suma de los divisores de", n, "es: ",suma_divi)