#Ejercicio 3 F
#Definir una función llamada divisores que tome un entero y devuelva la lista de divisores de
#ese entero.


def divisores(entero):
    divisores=[]
    for i in range(1,entero+1):
        if entero%i==0:
            divisores.append(i)
    return divisores


print (divisores(10))
