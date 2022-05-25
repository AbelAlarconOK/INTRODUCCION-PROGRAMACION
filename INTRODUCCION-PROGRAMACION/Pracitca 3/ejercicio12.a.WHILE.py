#Ejercicio 12
#a) Hacer un programa que permita al usuario elegir un número positivo n y luego
#muestre en pantalla los n primeros términos de la sucesión an = 2n. Es decir 2, 4,
#6...

n=int(input("ingrese un numero positivo: "))
i=1
while i <=n:
    if n<=0:
     print(2*i)
    i=i+1



