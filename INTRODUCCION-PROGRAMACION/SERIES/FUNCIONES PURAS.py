#FUNCIOINES PURAS: USAN RETORNO.


#def dividir(n,m):
    #r=n/m
    #return r #retorna un valor/expresion

#programa principal (main).

#cuenta=dividir(10,2)
#print(cuenta)

#ABREVIADO
#def dividir(n,m):
    #return n/m #retorna un valor/expresion

#programa principal (main).
#n1=int(input())
#n2=int(input())
#print (dividir(n1,n2))


#FUNCION.
def dividir(n,m):
    return n/m


#PROGRAMA PRINCIPAL.
num=int(input("numerador: "))
den=int(input("denominador: "))

while (den!=0):
    r=dividir(num,den)
    print(r)
    num=int(input())
    den=int(input())


