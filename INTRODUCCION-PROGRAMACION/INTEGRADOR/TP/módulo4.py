
def suma(numeros):
    acumulador=10
    contador=0
    numerador=5
    exponente=3
    denominador=2
    for i in range(1,numeros+1):
        if contador==3:
            denominador=2

        termino=exponente
        acumulador=acumulador-(numerador/denominador**exponente)+termino
        exponente=exponente+2
        numerador=numerador+2
        contador=contador+1
    return acumulador


print(suma(2))