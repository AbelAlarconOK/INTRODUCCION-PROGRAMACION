#Ejercicio 10 F
#Escribir una función llamada maximoIndice que tome una lista de números y devuelva el
#índice del máximo elemento.

lista=[1,4,3,13,15,36,7,8,9,10,21,3]
#print (lista[4])


def maximoIndice(lista):
    indice=0
    mayor=0
    for i in range (len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
            indice=i
    return indice


print (maximoIndice(lista))


#for i in range (len(lista)):
    #print (lista[i]) IMPRIMER ELEMENTOS DE LA POSICION
    #print(i) IMPRIME POSICIONES(INDEICE)