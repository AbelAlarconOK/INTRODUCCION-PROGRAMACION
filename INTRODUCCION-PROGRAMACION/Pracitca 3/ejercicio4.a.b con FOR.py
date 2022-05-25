#Ejercicio 4
#a) Hacer un programa que muestre, mediante un ciclo, los numeros desde el 5 hasta el
#11 salteando de a 2 elementos (5, 7, 9 y 11)
#b) Hacer un programa que permita al usuario elegir un numero m y un n y luego
#muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
#usuario ingresara un n igual a 2 y un m igual a 14, el programa deberÃ¡ mostrar
#2, 5, 8, 11, 14.

#a
for i in range(5,11+1,2):
    print(i)

#b
n=int(input("ingrese un numero: "))
m=int(input("ingrese otro numero: "))

for i in range(n, m+1,+3):
    print(i)