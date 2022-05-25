#Ejercicio 4 F
#Definir una función llamada laMasCorta que tome dos listas y devuelva la que tenga menos
#elementos. Si tienen igual cantidad, deberá devolver la primera.

lista_1=[1,2,3,4,5,6,7,8,9,2,1,4,4,5,6,6]
lista_2=[1,2,3,4,5,6,7,8,9,10,11,12]

def laMasCorta(lista1,lista2):
    if len(lista1)<len(lista2):
        return lista1
    else:
        return lista2
print  (laMasCorta(lista_1,lista_2))