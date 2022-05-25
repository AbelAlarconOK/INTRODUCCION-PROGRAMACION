#Ejercicio 13 F
#Escribir una función llamada frecuencia que tome una lista de enteros s y otro entero n como
#parametros y devuelva la cantidad de veces que aparece n en s.



def frecuencia(lista,parametro):
    cont=0
    for i in range(len(lista)):
        if lista[i]==parametro:
            cont=cont+1
    return cont


numeros=[1,2,3,5,6,7,8,9,10,11,4,12,13]
b=4
print(frecuencia(numeros,b))