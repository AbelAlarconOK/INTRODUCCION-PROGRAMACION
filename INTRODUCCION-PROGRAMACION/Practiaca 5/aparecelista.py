#1- Hacer una funciÃƒÂ³n que recibe una lista y un entero e indique si el entero estÃƒÂ¡ en la lista.



def esta(lista,entero):
    for i in lista:
        if i==entero:
            return True
    else:
        return False

lista_enteros=[1,2,3,4,5,6,7,8,9]
numero=10

if entero(lista_enteros,numero)==True:
    print(numero,"esta repetida")
else:
    print(numero,"No esta repetida")


