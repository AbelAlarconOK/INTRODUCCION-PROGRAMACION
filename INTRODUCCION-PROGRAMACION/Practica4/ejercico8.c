#funciones:
#factoes primos:ejercicio8 c:

def factoresPrimos(n):
    for i in range(2,n+1):
        if n%i==0:
            n=n/i
            print(i)


#pp
n=int(input("ingrese un valor: "))
factoresPrimos(n)#!








