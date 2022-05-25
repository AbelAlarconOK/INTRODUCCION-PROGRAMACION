#Ejercicio 14 F
#Definir una función llamada interseccion que tome dos listas sin repetidos y devuelva una
#nueva lista que contenga sólamente aquellos elementos que estén ambas listas.

def intersecciones(lista,lista2):
    nueva=[]
    for i in range(len(lista)):
        for j in range(len(lista2)):
            if lista[i]==lista2[j]:
                nueva.append(lista2[j])
    return nueva





numeros2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
numeros=[6,7,8,9,10,11,12,13,14,15,16]

print(intersecciones(numeros,numeros2))
