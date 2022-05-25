#Ejercicio 11
#a) Hacer una función que sume los divisores propios de un número.
#b) Hacer una función que indique si un número es perfecto. Número perfecto: a es
#perfecto si la suma de sus divisores propios es igual a.
#c) Hacer una función que determine si un número ingresado por el usuario es un número
#abundante. Número abundante: todo número natural que cumple que la suma de sus
#divisores propios es mayor que el propio número. Por ejemplo, 12 es abundante ya
#que sus divisores son 1, 2, 3, 4 y 6 y se cumple que 1+2+3+4+6=16, que es mayor
#al propio 12.

#def sumaDivisores(numero):
#    suma=1
#    for i in range(2,numero+1):
#        if numero %i ==0:
#            suma=suma+i
#    return suma
#print(sumaDivisores(14))


def perfecto(n):
    suma=1
    for i in range(2,n):
        if n %i==0:
            suma=suma+i
    if suma ==n:
        return True
    else:
        return False

print(perfecto(5))