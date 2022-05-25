#Ejercicio 11 F
#Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
#ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
#vericar los resutlados

n1=int(input("Ingrese el primer numero: " ))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("ingrese el tercer numero: " ))

if n1>n2 and n1>n3:
    print(n1)
else:
    if n2>n3 and n2>n1:
        print(n2)
    else:
        print(n3)



n1=int(input("Ingrese el primer numero: " ))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("ingrese el tercer numero: " ))

if n1>n2 and n2>n3:
    print(n1)
else:
    print(n2)
    if n3 >n2:
        print(n3)
