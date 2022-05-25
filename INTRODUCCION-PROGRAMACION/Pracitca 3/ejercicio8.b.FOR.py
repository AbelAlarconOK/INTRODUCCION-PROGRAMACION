#b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
#potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
#16 32.

n=int(input("ingrese un numero: "))

for i in range(n):
    if 2**i<=n**2:
        print(2**i)
