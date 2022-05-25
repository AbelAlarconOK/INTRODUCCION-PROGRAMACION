#Modificar el programa anterior para, para que pida al usuario un numero entero
#e imprima la tabla de multiplicar de dicho numero.

a = int (input ("Ingrese un numero"))#numero que decea multiplicar.
b = int (input ("Ingrese un numero"))#por cuanto decea multiplicar.
i = 1
while (i <= b):
    print (a, "x", i, "=", i * a)
    i= i + 1