#Ejercicio 9
#a) Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla todos los divisores de n.

n=int(input("ingrese un numero positivo: "))
for i in range (1,n+1,+1):
        if n%i==0:
            print("los divisores de son:",i)

