#Ejercicio 9 F
#Escribir una función llamada maximo que tome una lista de números y devuelva el valor del
#máximo elemento.

numeros=[1,0]

def max(lista):
    mayor=lista[0]
    for n in range (len(lista)):
        if lista[n]>mayor:
            mayor=lista[n]
    print(mayor)




max(numeros)


