#Ejercicio 8 F
#d) Hacer una funciÃƒÂ³n (no pura) que reciba un entero e imprima sus factores primos.
#Por ejemplo para a = 20 la funciÃƒÂ³n debe mostrar 2 y 5.
#Nota: Los nÃƒÂºmeros primos son aquellos cuyos ÃƒÂºnicos divisores positivos son ellos
#mismos y el 1.


def factoresPrimos(numero):
    for i in range(2,numero+1):
        while numero%i==0:
            numero=numero/i
            print(i)

n=int(input("ingrese un numero: "))
factoresPrimos(n)



