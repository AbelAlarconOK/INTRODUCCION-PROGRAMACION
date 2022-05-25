#determinar si un numero ingresado por el usuario es primo.
#un numero primo: tiene, extactamente, 2 divisores positivos.
#1 y si mismo.
#ej 5 es primo, pues unico dos divisores 5, 1.

#¿cuando un numero divide a otro?
#sea n un natural, i otro natural, i divide a n si el rseto de dividir a n por i
#es 0(y obtenemos un cociente entero).

#EJ 10.
#¿caules son los candidatos divisores de 10?
#[1,10]=1,2,3,4,5,6,,7,8,9,10.

#¿cuales son los divisores de 10?
#Divisores de 10: 1,2,5,10

n=int(input("ingresar un valor para n: "))

cont_divisores=0 #cantidad de divisores de n
for i in range (1,n+1):
    #resto=n%i variable.
        if n%i==0:#se encontro un divisor de n.
             cont_divisores=cont_divisores+1#se incrementa en 1 la cantidad de divisores.
if cont_divisores > 2:
    print(n,"no es primo")
else:
    print(n,"es primo")