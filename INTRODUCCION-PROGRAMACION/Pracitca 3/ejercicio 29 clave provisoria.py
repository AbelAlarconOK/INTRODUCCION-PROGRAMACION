#Ejercicio 29
#Hacer un programa que genere una clave provisoria para la gestión online de clientes de una
#empresa. El programa le pedirá el apellido y generará una clave de 5 caracteres, tomará las
#primeras 4 consonantes de la palabra ingresada. Cuando las consonantes no alcancen a 4, las
#faltantes las reemplazará por "*". Ejemplos:
#clemente CLMN
#rivera RVR*
#oreo R***
#La clave se completará con 1 dígito generado aleatoriamente entre 0 y 9.
#Ejemplos: CLMN1 RVR*4 R***7

#consonante=todas las del abecedario menos las vocales.

import random

numero=random.randint(0,9)
numero=str(numero)

apellido="alarcon"
clave_provisoria=""
vocales="aeiou"

for i in apellido:
    if  i not in vocales:
        clave_provisoria=clave_provisoria+i

        while len(clave_provisoria)==4:
            clave_provisoria=clave_provisoria+"*"
            print(clave_provisoria+numero)
