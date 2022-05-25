#Ejercicio 14
#Hacer un programa que solicite al usuario un numero entero positivo e indique cual es el
#numero primo mayor mas cercano. Usar funciones. Por ejemplo, si el usuario ingresa 24, el
#programa devolvera 29 (29 es el numero primo mas cercano mayor que 24). Si el usuario ingresa
#5 el programa devolvera 7.


def primo(numero):
    if numero<2:
        return False
    for i in range(2,numero):
        if numero%i==0:
            return False
    return True

#
n=10000
primernumero=[]
for i in range(n+1,n+n):
    if primo(i)==True:
        primernumero.append(i)
print(primernumero[0])


#mejor forma.
n=24
i=n+1
encontrado=False
while  encontrado==False:
    if primo(i)==True:
        encontrado=True
        print (i)
    i=i+1

