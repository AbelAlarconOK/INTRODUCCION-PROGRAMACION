from principal import *
from configuracion import *

import random
import math

def estaCerca(x,lista):
    #mantiene las letras distantes

        for i in range(0,len(lista)):

            if(x<lista[i][0]+10 and x>lista[i][0]-10):#si la nueva coordenada "x" esta entre +10 y -10
                if(lista[i][1]!=0):
                    if lista[i][1]<3 and lista[i][1]>0:#si la nueva coordenada "Y" esta entre 0 y 3 de esa misma coordenada encontrada.
                        lista[i][1]=40#alejamos la letra antigua en el eje vertical 40 lugares


def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    #elige una palabra de la lista y la carga en las 3 listas
    # y les inventa una posicion para que aparezca en la columna correspondiente

    for i in range (0,1):#cantidad de palabras a cargar
        coordenadas=[]
        elemento=random.randrange(1,len(lista))#tomamos al azar un numero para indexar un elemento de la lista
        elemento=lista[elemento]
        largoElemento=len(elemento)

        print(elemento)#ESTE PRINT ES PARA CONTROLAR LAS PALABRAS QUE SALEN. TENEMOS QUE BORRARLO

        randomNum=random.randrange(0,largoElemento)#al azar usarmeos este numero para dividir la palabra

        for i in range(0,randomNum):#recorremos la palabra hasta donde marque el numero random
            #guardamos la letra en la lista izquierda
            listaIzq.append(elemento[i])
            #guardamos las coordenadas en la lista de coordenadas
            coordenadaX=random.randrange(2,250)
            coordenadaY=2
            estaCerca(coordenadaX,posicionesIzq)
            posicionesIzq.append([coordenadaX,coordenadaY])

        if randomNum+1<largoElemento:#si quedaron letras de la palabra repetimos el metodo para seguir repartiendo en las listas
            randomNum2=(random.randrange(randomNum+1,largoElemento))#numero para usar de indice para las letras que restan de la palabra
        else:
            randomNum2=largoElemento

        for i in range(randomNum,randomNum2):#recorremos la palabra segun los nuevos margenes
            #guardamos la letra en la lista del medio
            listaMedio.append(elemento[i])
            #guardamos las coordenadas en la lista de coordenadas
            coordenadaX=random.randrange(270,520)
            coordenadaY=2

            estaCerca(coordenadaX,posicionesMedio)
            posicionesMedio.append([coordenadaX,coordenadaY])

        for i in range(randomNum2,largoElemento):#recorremos la ultima parte de la palabra
            #guardamos la letra en la lista derecha
            listaDer.append(elemento[i])
            #guardamos las coordenadas en la lista de coordenadas
            coordenadaX=random.randrange(535,780)
            coordenadaY=2

            estaCerca(coordenadaX,posicionesDer)
            posicionesDer.append([coordenadaX,coordenadaY])


def bajar(lista, posiciones):
# hace bajar las letras y elimina las que tocan el piso
    vel=10

    if len(lista)>0:# si la lista no esta vacia

        for i in range(0,len(lista)):

            if posiciones[i][1]!=0:#si la letra no llego al piso
                posiciones[i][1]=posiciones[i][1]+vel#baja "x" cantidad de casilleros
                if posiciones[i][1]>500:#si la letra llego al piso
                    posiciones[i][1]=0#se coloca en la coordenada "Y" un 0(cero),como marca, para que luego sea omitida a la hora de dibujarla.

def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    ## llama a otras funciones para bajar bajar las letras, eliminar las que tocan el piso y
    ## cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letrasla pantalla)
    bajar(listaIzq,posicionesIzq)
    bajar(listaMedio,posicionesMedio)
    bajar(listaDer,posicionesDer)

    tiempoSegundos=int(pygame.time.get_ticks()/1000)


    if tiempoSegundos%5==0:
        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)





def Puntos(candidata):
 puntos=0

 for i in range(len(candidata)):
   if candidata[i]=="a"or candidata[i]=="e" or candidata[i]=="i" or candidata[i]=="o" or candidata[i]=="u":
     puntos+=1
   elif candidata[i]=="b" or candidata[i]=="c" or candidata[i]=="d" or candidata[i]=="f" or candidata[i]=="g" or candidata[i]=="l" or candidata[i]=="m" or candidata[i]=="n" or candidata[i]=="p" or candidata[i]=="r" or candidata[i]=="s" or candidata[i]=="t" or candidata[i]=="v":
    puntos+=2
   elif candidata[i]=="j" or candidata[i]=="k" or candidata[i]=="q" or candidata[i]=="w" or candidata[i]=="x" or candidata[i]=="y" or candidata[i]=="z":
    puntos+=5
 return puntos

    #devuelve el puntaje que le corresponde a candidata

def procesar(lista, candidata, listaIzq, listaMedio, listaDerecha):
    puntaje=0
    for i in range(len(lista)):
        if lista[i]==candidata:
            puntaje=Puntos(candidata)
            return puntaje
    else:
        return puntaje

    #chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta


def esValida(lista, candidata, listaIzq, listaMedio, listaDerecha):
    nueva=""
    for elemento in listaIzq:
        nueva=nueva+elemento
    for elemento in listaMedio:
        nueva=nueva+elemento
    for elemento in listaDerecha:
        nueva=nueva+elemento
    if nueva==candidata:
        return  True
    else:
        return False



    #devuelve True si candidata cumple con los requisitos
