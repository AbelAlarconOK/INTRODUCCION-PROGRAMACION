#Ejercicio de ejemplo 1
#Hacer en papel y luego en Python un programa que pida un entero entre 1 y 10
#utilizando elmensaje Adiviná en qué número estoy pensando!,
#y muestre Adivinaste si el usuario ingresael número 7

n=int(input("adivina que numeo estoy pensando"))
if (n==7):
    print("adivinaste")

#Ejercicio de ejemplo 2
#Modificar el programa del ejercicio anterior para que en caso de que el usuario
#no adivine elnúmero, muestre por pantalla el mensaje Perdiste.

n=int(input("adivina que numeo estoy pensando"))
if (n==7):
    print("adivinaste")
else:
    print("perdiste")

#Ejercicio de ejemplo 3
#Modicar el programa del ejercicio anterior para que en caso de que el usuario
#ingrese unvalor menor a 7 muestre Te quedaste corto y en caso de ingresar
#algo mayor a 7 muestre . Tepasaste.

n=int(input("adivina que numeo estoy pensando"))
if (n==7):
    print("adivinaste")
else:
    if (n>7):
        print("te pasaste")
    else:
            print("te quedaste corto")
