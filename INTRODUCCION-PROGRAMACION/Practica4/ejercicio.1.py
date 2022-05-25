#Ejercicio 1 F
#Hacer un programa para cada inciso que pida al usuario un número decimal x y muestre por
#pantalla el resultado de evaluar las siguientes fórmulas:
#a) √x
#b) |x|
#c) |x − 3|
#d) √|x − 5|


#funcion
def raizCuadrada(valor):
    import math
    return math.sqrt(valor)

#pp
#n=int(input(""))
#print(raizCuadrada(n))


#funcioin

#def modulo(n1):
#    return (abs(n1))

#n=int(input(""))
#print (modulo(n))


def RaizModulo(n1):
    import math
    return (math.sqrt(abs(n1-3)))

n=int(input(""))
print(RaizModulo(n))




