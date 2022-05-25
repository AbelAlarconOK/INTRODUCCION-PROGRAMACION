#-------------------------------------------------------------------------------
# Name:        Ejercicio 17.
# Purpose:
#
# Author:      Abel
#
# Created:     23/08/2021
# Copyright:   (c) Abel 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#La empresa que administra los cajeros automÃƒÂ¡ticos lo contrata para que programen
#la entrega debilletes, el usuario ingresa sula cantidad de dinero que desea y
#usted debe indicar cuantos billetes de cadadenominaciÃƒÂ³n se debe entregar.
#Es importante entregar siempre la menor cantidad de billetes. Ayuda:
#El operador % da el resto de la divisiÃƒÂ³n a/b, y el operador // da la parte
#entera del cociente de a/b.


#Argentina tenemos billetes de / 1000 / 500 / 200 / 100.

dinero = int(input("dinero a retirar"))

#Calculo los billetes de 1000 y guardo el resto en resto1.

b1000 = dinero // 1000
resto1 = dinero % 1000
b500 = resto1 // 500
resto2 = resto1 % 500
b200 = resto2 //200
resto3 = resto2 % 200
b100 = resto3// 100
resto4 = resto3%100

print ("cantidad de billetes de 1000 ", b1000)
print ("cantidad de billetes de 500 ", b500)
print ("cantidad de billetes de 200 ", b200)
print ("cantidad de billetes de 100 ", b100)
print ("saldo restante: " , resto4)

#otra opcion
monto = int(input("cantidad de monto: "))

b1000 = 1000
b500 = 500
b200 = 200
b100 = 100

#2800
cant_b1000 = monto // b1000
monto = monto % b1000 # 800 -> monto

#monto800
cant_b500 = monto // b500 #800//500 = 1
monto = monto % b500 # monto

cant_b200 = monto // b200
monto = monto % b200

cant_b100 = monto//b100
monto = monto % b100

print ("cantidad de billetes de 1000: ", cant_b1000)
print("cantidad de billetes de 500: ", cant_b500)
print("cantidad de billetes de 200: ", cant_b200)
print("cantidad de billetes de 100: ", cant_b100)
























