#Ejercicio 12 F
#Escribir una función llamada intercambiar que tome una lista de números s y dos enteros
#positivos a y b menores que la longitud de la lista y cambie el elemento ubicado en s[a] por el
#elemento ubicado en s[b]. Ojo, esta función no debe devolver una lista, sino modifcar la que
#toma como parámetro.


def intercambiar(n1,n2,lista):
    for i in range(len(lista)):
        lista[n1]=lista[n2]
    return lista
#pp

numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13]
a=2
b=6
intercambiar(a,b,numeros)
print(numeros)