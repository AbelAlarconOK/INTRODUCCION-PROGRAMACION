#2- Hacer una funciÃ³n que dado un entero y una lista de enteros indique
#cuantas veces aparece el entero en la lista.

def vecesAparece(lista,numero):
    cont=0
    for i in lista:
        if i==numero:
            cont=cont+1
    return cont

lista_numeros=[1,2,3,4,5,6,7,8,9,2,4,6,3]
entero=4

print (vecesAparece(lista_numeros,entero))