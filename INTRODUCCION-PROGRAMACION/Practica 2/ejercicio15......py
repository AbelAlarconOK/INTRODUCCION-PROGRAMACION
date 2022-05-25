#Ejercicio 15 F Ã¢â„¢Â£
#Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
#El programa debera¡ luego hacer que en la variable a quede el menor de los valores recibidos, en
#b el intermedio y en c el mayor (es decir, ordenar a los valores).
a = int(input("Ingrese una variable"))
b = int(input("Ingrese una variable"))
c = int(input("Ingrese una variable"))

if a >b:
    aux=b
    b=a
    a=aux
if a >c:
    aux=c
    c=a
    a=aux
if b>c:
    aux=c
    c=b
    b=aux
print(a,b,c)