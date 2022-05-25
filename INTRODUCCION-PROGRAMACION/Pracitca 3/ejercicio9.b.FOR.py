#b) Hacer un programa que permita al usuario elegir un nÃºmero positivo n y luego
#muestre en pantalla todos los divisores pares de n.

n=int(input("ingrese un numero positivo: "))

for i in range(1,n+1,+2):
    if n%i==0:
        print(i)

for i in range(1,n+1):
     if n%i==0 and i%2==0:
        print(i)