#Ejercicio 14 F
#Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
#primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
#valores de las variables y mostrarlos de mayor a menor.


n1=int(input("primer numero entero: "))
n2=int(input("segundo numero enter: "))

v1=n1
v2=n2

if v1>v2:
    print(v1,v2)
else:
    print(v2,v1)

aux=v1
v1=v2
v2=aux

print(v1,v2)