#Ejercicio 7 F
#Defnir una función llamada dondeAparece que tome una lista de enteros y un entero llamado
#blanco como parámetros, y devuelva el primer índice donde blanco aparece en el arreglo, si lo
#hace, y -1 en caso contrario.

enteros=[1,2,3,4,5,6,7,8,9]
blanco=6

def doneAparece(enteros,blanco):
    for n in range (len(enteros)):
        if (enteros[n] ==blanco):
            return n
    return -1


print (doneAparece(enteros,blanco))
