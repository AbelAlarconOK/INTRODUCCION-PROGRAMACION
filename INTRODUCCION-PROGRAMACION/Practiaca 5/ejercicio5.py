#Ejercicio 5 F
#Definir una funciÃ³n llamada sonFactores que tome un entero n y una lista de enteros, y
#devuelva True si los nÃºmeros de la lista son factores de n (es decir, si n es divisible por todos
#ellos).

lista_enteros=[1,2,4,5,6]
entero=120


#print (lista_enteros[0]*lista_enteros[1])
lista_divisores=[]
def sonFactores(lista,entero):
    for i in (lista_enteros):
        if entero %i==0:
            lista_divisores.append(i)
    if len (lista_enteros)==len(lista_divisores):
        return True
    else:
        return False

print (sonFactores(lista_enteros,entero))


