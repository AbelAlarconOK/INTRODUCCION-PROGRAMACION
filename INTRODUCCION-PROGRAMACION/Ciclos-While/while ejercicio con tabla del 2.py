#Realizar un prograa que imprima la tabla del 2, desde el 1 al 10.

a = int (input ("Ingrese un numero"))#numero que decea multiplicar.
b = int (input ("Ingrese un numero"))#por cuanto decea multiplicar.
i = 1
while (i <= b):
    print (a, "x", i, "=", i * a)
    i = i + 1