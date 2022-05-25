#FUNCIONES:estan hechas.

#import random: aleatorios.

#import math: funciones matematicas.

#random.randrange(1,100,3) -> argumentos.

#print("holamundo", end="")

#math.log(2).

#math.log(math.sqrt(abs(-10))).


#

def MiFuncion():#adentro de los parentesis.(PARAMETRO)
    print("hola mundo")

def MostrarUnmensajes(msg):
    print(msg)

def Sumar(v1,v2):
    v3=v1+v2
    print(v3) #FUNCIONRS IMPURAS USAN PRINT.

#programa principal:--> activar a las funciones o llamar a las funciones.

#MiFuncion()#argumentos
#dato=input("ingresar una palabra: ")
#MostrarUnmensajes(dato)

n=int(input())
m=int(input())
Sumar(n,m)#tener en cuenta el orden de los argumentos y los parametros.

