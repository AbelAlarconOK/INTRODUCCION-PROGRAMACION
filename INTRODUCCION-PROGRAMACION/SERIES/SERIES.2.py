#SERIES:
#1/2 + 2/3 + 3/4 +........


#ZONA FUNCIONES:

def sumaSerie(n):
    acumulador_suma=0

    for numerador in range(1,n+1):
        acumulador_suma=acumulador_suma+(numerador/(numerador+1))

    return acumulador_suma

#programa
n=int(input("ingrese la cantidad de terminos:"))
print(sumaSerie(n))

