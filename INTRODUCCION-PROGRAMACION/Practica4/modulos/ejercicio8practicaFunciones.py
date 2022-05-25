#Ejercicio 8 F
#a) Escribir una función que tome un parámetro de tipo entero y devuelva la cantidad
#de divisores positivos de ese número.
#b) Escribir una función que tome un parámetro de tipo entero y devuelva el valor True
#si se la llama con un número primo y False en caso contrario.
#c) ¾Cuál es el número primo más grande que encontraste?
#d) Hacer una función (no pura) que reciba un entero e imprima sus factores primos.
#Por ejemplo para a = 20 la función debe mostrar 2 y 5.
#Nota: Los números primos son aquellos cuyos únicos divisores positivos son ellos
#mismos y el 1.


#def divisores(numero):
#    cant_divisores=0
#    for i in range(1,numero+1):
#        if numero%i==0:
#            cant_divisores=cant_divisores+1
#    return cant_divisores
#print(divisores(10))


def booleanos(numero):
    cont=0

    for i in range(1,numero+1):
        if numero%i==0:
            cont=cont+1
            print(i)
    if cont ==2:
        return True
    else:
        return False


print(booleanos(5))
