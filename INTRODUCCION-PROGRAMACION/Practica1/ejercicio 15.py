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
#Ejercicio 15 F
#Un vendedor recibe un sueldo base de $22000 más un 10 % extra del total de sus
#ventas, el vendedordesea saber cuánto dinero obtendrá en total en el mes si ha
#logrado realizar 3 ventas este mes. Tenga encuenta el sueldo básico y la
#comisión por las ventas. Hacer un programa que solicite el monto de cada
#una de las ventas del mes e indique cuál será el sueldo final del vendedor.

sueldo = 22000
venta1 = 1000
venta2 = 2000
venta3 = 1500
extra = venta1+venta1+venta3*0.10
total = sueldo+extra
print("usted ganara: " , total)
