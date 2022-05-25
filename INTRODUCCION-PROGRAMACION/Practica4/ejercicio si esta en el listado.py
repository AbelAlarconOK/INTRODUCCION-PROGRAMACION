#escribir una funcion esta(listam,elemento)y verifique si dicho elemento pertenece
#a la lista, si pertence, retorna true, caso contrario, false.

#funcion:

def esta(lista,elemento):
    for elem in lista:
        if elem==elemento:
            return True
    else:
        return False


#pp
frutas=["manzana", "pera", "banana", "naranja"]

elemento=input("ingrese el nombre de una fruta: ")

if esta(frutas,elemento):
    print("la fruta ",elemento,"esta en el listado.")
else:
    print("la fruta ", elemento,"No esta en el listado.")