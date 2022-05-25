#Ejercicio 15 F
#Definir una función llamada union que tome dos listas sin repetidos y devuelva una nueva lista
#que contenga los elementos de ambas listas. Ojo, la lista de retorno debe no tener repetidos.

def union(lista,lista2):
    nueva=[]
    for i in range(len(lista)):
        for j in range(len(lista2)):
            if lista[i] not in nueva:
                nueva.append(lista[i])
            if lista2[j] not in nueva:
                nueva.append(lista2[j])
    return nueva

numeros2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
numeros=[6,7,8,9,10,11,12,13,14,15,16,17]

print(union(numeros2,numeros))
