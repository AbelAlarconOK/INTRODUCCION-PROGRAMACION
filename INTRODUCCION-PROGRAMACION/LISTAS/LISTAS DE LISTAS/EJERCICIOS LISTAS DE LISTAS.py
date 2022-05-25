#EJERCICIO LISTAS DE LISTAS:

#MATRIS

#1_ESCRIBIR LA LISTA EB TABLA/MATRIZ.
tabla= [

    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]

 ]
#2_OBTENER EL PROMEDIO DE LA TOTALIDAD DE ELEMENTOS.
promedio=0
cant_elemento=0
for fila in range(len(tabla)):
    for columna in range(len(tabla)):
        promedio=promedio + tabla[fila][columna]
        cant_elemento=cant_elemento+1
#print(promedio/cant_elemento, end="")

#IMPRIMI LA SUMA DE LOS ELEMENTOS DE LA PRIMER FILA.
suma=0

for elem in tabla[0]:
    suma=suma+elem
print(suma)

#IMPRIMIR LA SUMA DE LOS ELEMENTOS DE LA ULTIMA FILA.
suma1=0

for elemt in tabla[len(tabla)-1]:
    #print(elemt)
    suma1=suma1+elemt
print(suma1)

