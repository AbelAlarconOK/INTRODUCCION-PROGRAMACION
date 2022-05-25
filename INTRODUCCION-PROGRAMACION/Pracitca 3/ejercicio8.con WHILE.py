#Ejercicio 8
#a) Hacer un programa que reciba un nÃƒÂºmero n y muestre todas las potencias de 2
#menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrarÃƒÂ¡: 1 2 4 8
#16. Ayuda: pensar primero si serÃƒÂ­a mÃƒÂ¡s prÃƒÂ¡ctico utilizar la sentencia while o for.

n=int(input("ingrese un numero: "))
i=1
potencia=0
while n>potencia:
    potencia=2**i
    if potencia<n:
         print(potencia)
    i=i+1




