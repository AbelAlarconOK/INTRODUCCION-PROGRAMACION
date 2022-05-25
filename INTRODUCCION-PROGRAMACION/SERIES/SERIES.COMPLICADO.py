#-2 * (1/2**2) + 2 * (2**3/4**4) - 2 * (4**5/8**6) +.....



#ZONA FUNCNION.

def sumaserie(n):
    acumulador_suma=0

    CONSTANTE_DOS=2

    singo=-1

    for i in range(0,n):

      numerador= (2**i)**(2**i+1)
      denominador=(2**(i+1))**(2*(i+1))

      producto=singo*(CONSTANTE_DOS*
      (numerador/denominador)

      acumulador_suma = acumulador_suma+producto

      singo = singo *(-1)

    return acumulador_suma

#programa

n=int(input("ingrese la cant.de terminas a calcular: "))

print(sumaserie(n))
