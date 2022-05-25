#c) Hacer un programa que permita al usuario elegir un número n, un m y un p y
#luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
#ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
#el programa deberá mostrar 2, 6, 10, 14.


m=int(input("ingrese un numero: "))
n=int(input("ingrese otro numero: "))
p=int(input("ingrese otro numero: "))
i=m

while i<=n and m:
    print(i)
    i=i+p


