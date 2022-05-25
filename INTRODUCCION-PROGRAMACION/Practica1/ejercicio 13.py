#-------------------------------------------------------------------------------
# Name:       Practica 1
# Purpose:
#
# Author:      Dario
#
# Created:     23/08/2021
# Copyright:   (c) Dario 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Ejercicio 13 F
#Suponga que una persona desea invertir su capital en un banco y quiere saber
#cuánto dinero tendrá ensu cuenta si el banco incrementa el 6 % mensual
#(no acumulativo). Se le debe pedir al usuario el capitala invertir
#y la cantidad de meses

capital = float(input("Cuano dinero desea invertir:"))
meses = int(input ("Y en cuantos meses:"))
incremento = capital+capital*0.06* meses
print ( "El dinero que resivira sera:", incremento)