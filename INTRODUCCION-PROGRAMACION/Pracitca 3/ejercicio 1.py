#Parte 1  Programas que muestran números
#Ejercicio 1
#a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales
#(1, 2, 3, 4 y 5).
#b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
#primeros n números naturales (1, 2, · · · , n).

#a
i=1
while i<=5:
    print(i)
    i=i+1

#b
n=int(input("ingrese un numero mayor a cero: "))
i=1
while i<=n:
    print(i)
    i=i+1

