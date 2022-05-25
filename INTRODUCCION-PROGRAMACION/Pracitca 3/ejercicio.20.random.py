#Ejercicio 20
#Hacer un programa que simule el juego de la quiniela. El usuario debe elegir un número del
#0 al 99 y un monto a apostar, si acierta el número gana 70 veces lo apostado. (El número de la
#suerte debe ser elegido al azar)


n=int(input("ingrese un numero al azar: "))
m=int(input("dinero a apostar: "))

m=m*70

while n <0 or n>99:
    print("error")
    n=int(input("ingrese un numero entre 0 y 99: "))

import random
#for j in range(3):cuantas veces repetir la jugada

i=random.randint(0,99)
if n==i:
    print("felizidade el numero ganador es: ",i,"\n" "tu ganacia es de: ",m)
else:
    print("el numero ganador es:", i)

