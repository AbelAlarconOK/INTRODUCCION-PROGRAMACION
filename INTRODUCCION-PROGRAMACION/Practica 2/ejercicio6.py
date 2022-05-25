#Ejercicio 6
#a) Escribir en papel un programa que pida al usuario dos numeros, y que muestre en
#pantalla al mayor de ambos. Luego hacer 3 corridas de escritorio, luego pasarlo a
#Python y por ultimo correr el programa con los valores iniciales de las corridas y
#vericar que funciona como se esperaba.
#b) Idem anterior pero para encontrar el menor

#a

n1 = int(input("ingrese primer numero: "))
n2 = int(input("ingrese segundo numer: "))

if n1 > n2:
    print (n1)
else:
    if n2 > n1:
        print (n2)
    else:
        print("son iguales")

#b

n1 = int(input("ingrese primer numero: "))
n2 = int(input("ingrese segundo numer: "))

if n1 < n2:
    print (n1)
else:
    if n2 < n1:
        print (n2)
    else:
        print("son iguales")