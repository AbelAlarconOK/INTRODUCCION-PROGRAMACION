#c) Hacer un programa que permita al usuario elegir un nÃºmero positivo n y luego
#muestre en pantalla la cantidad de divisores de n.

n=int(input("Ingrese un numero positivo: "))
contador=0
for i in range(1,n+1):
    if n%i==0:
        contador=contador+1
print("La cantida de divisores de ", n, "son", contador)