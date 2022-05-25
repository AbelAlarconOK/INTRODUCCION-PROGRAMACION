#Ejercicio 8 F
#Hacer una función que tome una lista de números decimales y devuelva el promedio de los
#elementos.
decimales=[1.5,2.3,4.1]
def promedioDecimales(lista):
    suma=0
    promedio=0
    for i in lista:
        suma=suma+i
        promedio=suma/len(lista)
    print(promedio)

promedioDecimales(decimales)