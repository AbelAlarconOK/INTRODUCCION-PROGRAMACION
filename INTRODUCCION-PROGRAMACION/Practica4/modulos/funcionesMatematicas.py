#Ejercicio 4 F
#a) Escribir una función que reciba dos números reales como parámetros y retorne su
#promedio.

#c) Idem de los dos anteriores pero con tres números. Escribir la función en el mismo
#archivo donde se escribió la del item a.


def promedio2(n1,n2):
    return (n1+n2)/2

def promedio3(n1,n2,n3):
    return (n1+n2+n3)/3

#Ejercicio 5 F
#Defnir una función que devuelva el valor absoluto de un número. (Hacerlo sin utilizar la
#función abs)


def valorAbsoluto(numero):
    if numero >=0:
        return numero
    else:
        return - numero
