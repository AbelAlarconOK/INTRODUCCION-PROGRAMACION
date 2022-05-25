#Ejercicio 1
#Este programa chequea una serie de condiciones para los tres valores ingresados
#por el usuario.Correrlo tal cual está en Python. Luego reemplazar donde dice
#True por una expresión lógicaque sea True o False según corresponda,
#en lugar de siempre True como ahora.

a = int(input("ingrese un numero entero"))
b = int(input("Ingrese un numero entero"))
c = int(input("Ingrese un numero entero"))
print("sted ingresó los valores:", a, b, c)
print(a, "es mayor que", b, True)
print(a, "y", b, "son iguales", False)
print(a, "es el mayor de todos", True)
print(b, "es el menor de todos", False)
print(a, "es mayor que alguno de los otros dos", True)
print(a, "es menor o igual que alguno de los otros dos", False)
print("Los tres numeros son iguales", False)
print("Los tres numeros son distintos", True)
print(a, "es par", False)
print("alguno es par", True)
print("ninguno es par", False)
print("todos son pares", False)
print(a, "es multiplo de 3", True)
print(a, "es multiplo de 3 y de 5", True)
print(a, "es multiplo de 3 y par", False)
print(a, "-", b, "da un numero positivo", False)
print(a, "-", b, "da un numero par positivo", True)