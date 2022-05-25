#Ejercicio 15 F ♣
#Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
#El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
#b el intermedio y en c el mayor (es decir, ordenará los valores).

a = int(input("Ingrese una variable"))
b = int(input("Ingrese una variable"))
c = int(input("Ingrese una variable"))

# asumimos que los tres son distintos

if a>b:
  if a>c:
    mayor=a
    if b>c:
        medio=b
        menor=c
    else:
        medio=b
        menor=c
  else:
    mayor=c
    medio=a
    menor=b
else:
    if b>c:
        mayor=b
        if a>c:
            medio=a
            menor=c
        else:
            medio=c
            menor=a
    else:
        mayor=c
        medio=b
        menor=a

print("El mas grande es ", mayor,
    "\nEl del medio es ", medio,
    "\nEl mas chico es", menor)
