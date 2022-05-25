def sumaDeSerise(numero):
    suma=0
    CONSTANTE=2
    signo=-1
    for i in range(1,numero+1,2):
        numerador=i**i
        denominador=i
        multiplicacion=signo*(CONSTANTE*(numerador/denominador))
        suma=suma+multiplicacion
        CONSTANTE=CONSTANTE+2
    return suma


#PP
n=int(input(""))
while n==0 or n<0:
    n=int(input("ingrse un numero positivo"))

print (sumaDeSerise(n))