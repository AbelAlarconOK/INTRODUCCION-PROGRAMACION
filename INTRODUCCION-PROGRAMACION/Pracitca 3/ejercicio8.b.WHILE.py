#b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
#potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
#16 32.

n=int(input("ingrese un numero: "))
i=1
while n<=0:
    n=int(input("ingrese otro numero: "))
while i <=n**2:
    print(i)
    i=2*i