#Ejercicio 8
#a) Hacer un programa que reciba un nÃºmero n y muestre todas las potencias de 2
#menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrarÃ¡: 1 2 4 8
#16. Ayuda: pensar primero si serÃ­a mÃ¡s prÃ¡ctico utilizar la sentencia while o for.

n=int(input("ingrese un numero: "))
for i in range(n):
    if 2**i<=n:
        print(2**i)