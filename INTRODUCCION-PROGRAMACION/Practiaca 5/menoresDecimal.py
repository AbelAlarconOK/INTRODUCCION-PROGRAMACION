#Ejercicio 20 F
#a) Definir una función que tome una lista de números s y un número decimal x y
#devuelva la cantidad de elementos de s que sean menores que x.
#b) Si se pone como condición que s siempre esté ordenada de mayor a menor, ¿cómo
#podría modificarse el programa para que haga menos iteraciones?


def elementosMenores(lista,decimal):
    menores=[]

    for i in range(len(lista)):
        if lista[i]<x:
            menores.append(lista[i])
        return menores


lista=[10,9,8,7,6,5,4,3,2,1]
x=3.2

print(elementosMenores(lista,x))








