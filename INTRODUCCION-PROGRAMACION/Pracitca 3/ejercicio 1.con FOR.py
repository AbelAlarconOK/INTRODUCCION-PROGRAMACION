#Parte 1  Programas que muestran nÃºmeros
#Ejercicio 1
#a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 nÃºmeros naturales
#(1, 2, 3, 4 y 5).
#b) Hacer un programa que permita al usuario elegir un numero n y luego muestre los
#primeros n numeros naturales (1, 2, · · · , n).

#a
for i in range(1,5+1):
    print(i)

#b
n=int(input("ingrese un numero: "))
for i in range(1,n+1,):
    print(i)