#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dario
#
# Created:     23/08/2021
# Copyright:   (c) Dario 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Ejercicio 14 F
#Una empresa telefónica desea un programa para calcular el importe de
# sus clientes. Sabiendo que elcosto por comunicación es de $7 y por cada
# segundo se cobra $0, 5 hacer dicho programa. Se deben ingresar la cantidad
# de llamadas realizadas y el tiempo total de comunicación, el programa
#debe devolver al precio a cobrar.


llamadas = int (input("cantidad de llamadas"))
tiempo = int (input ("Indique cuanos segundos hablo"))
costoporsegundo = 0.5
precio =llamadas+tiempo*costoporsegundo
print( "su importe es:", precio)


cantLlamadas=int(input("Ingrese la cantidad de llamadas: "))
tiempo=int(input("Indique cuantos segundos hablo: "))
costoSegundo=0.01

precio=cantLlamadas+tiempo*costoSegundo

print("Usted recibira:$", precio)