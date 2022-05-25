#3- Hacer una función que reciba una lista de enteros y devuelva el máximo.
#sin utilizar funcion min,max.


enteros=[5,2,10,6,14]
def max(lista):
    mayor=lista[0]
    for n in lista:
        if n>mayor:
            mayor=n
    return mayor


print(max(enteros))

