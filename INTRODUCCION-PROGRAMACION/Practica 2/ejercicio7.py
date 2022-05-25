#Ejercicio 7
#Escribir en papel un programa que pida al usuario dos números de punto flotante y muestre
#su promedio. Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla
#Aprobado y si no, debe mostrar Desaprobado. Después de hacerlo en papel, pasarlo a Python.


n1 = float(input("primer numero:"))
n2 = float(input("segundo numero:"))

promedio = (n1 + n2) / 2

if promedio > 7:
    print ( "aprobado")
else:
    print ("desaprobado")



