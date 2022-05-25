#EJERCICIOS CONDICIONALES PRACTICA 02.

#1. Dado un nÃºmero indicar si es par o impar.
#2. Hacer un programa que solicite dos nÃºmeros e indique el signo de la
# multiplicaciÃ³n sin efectuarla.
#3.Introducir dos nÃºmeros enteros por el teclado, DIVIDENDO y DIVISOR.
# Si dividendo es divisible por divisor, el programa debe mostrar el mensaje
#â€œDIVISIBLESâ€ caso contrario â€œNO SON DIVISIBLESâ€.
#4.Dadas tres notas parciales. Indicar si se promociona, va a final o recursa.
#Sabiendo que:

#	[0,4)   - RecursA
#	[4,7)   - Final
#	[7-10] - Promociona

#1
numero = int(input("primer nota"))
if  (numero % 2 == 0):
     print (numero, " es par")
else:
    if ( numero % 2 != 0):
        print (numero, " es impar")

#operadores relacionales

+
-
<
>
==
!=

#operadores logicos

and #y, segunda prioridad
or # o, ultima prioridad
not # no, primer prioridad

elif
