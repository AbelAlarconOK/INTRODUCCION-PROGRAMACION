#SERIES.

#1+1/2+1/3+1/4.......+1/10.


#zona de funciones.
def sumaserie(n):
    acumulador_suma=0

    for i in range(1,n+1):
        acumulador_suma=acumulador_suma+(1/i)

    return acumulador_suma

#programa principal.

n=int(input("ingrese la cantidad de terminos a calcular: "))
print (sumaserie(n))
