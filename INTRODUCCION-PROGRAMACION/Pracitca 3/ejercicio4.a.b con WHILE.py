#Ejercicio 4
#a) Hacer un programa que muestre, mediante un ciclo, los nÃºmeros desde el 5 hasta el
#11 salteando de a 2 elementos (5, 7, 9 y 11)
#b) Hacer un programa que permita al usuario elegir un nÃºmero m y un n y luego
#muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
#usuario ingresara un n igual a 2 y un m igual a 14, el programa deberÃ¡ mostrar
#2, 5, 8, 11, 14.
#c) Hacer un programa que permita al usuario elegir un nÃºmero n, un m y un p y
#luego muestre todos los naturales entre m y n, pero salteando de a p nÃºmeros. Por
#ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
#el programa deberÃ¡ mostrar 2, 6, 10, 14.

#a
i=5
while i<=11:
    print(i)
    i+=2

#b
n=int(input("ingrese un numero: "))
m=int(input("ingrese otro numero: "))
i=n
while i <=m:
    print(i)
    i+=3

