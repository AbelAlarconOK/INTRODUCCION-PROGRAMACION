#Ejercicio 9 F
#Se tiene la siguiente lista con DNIs de personas.
#30612453
#23763290
#21448503
#34582048
#15364857
#Dado otro nÃºmero de DNI cualquiera, se desea construir un programa que determine si es alguno
#de los existentes en el listado. Escribir el programa en papel y luego pasarlo a Python.


dni=input("ingrese su numero de dni: ")

d1="30612453"
d2="23763290"
d3="21448503"
d4="23582048"
d5="15364857"

#primera forma.
if dni != d1 and dni!=d2  and dni!= d3 and dni!=d4 and dni!=d5:
    print("no se encuentra registrado")
else:
    print(" esta registrado")


#segunda forma.
if dni == d1 or dni==d2  or dni== d3 or dni==d4 or dni==d5:
    print("existe registrado")
else:
    print("no esta registrado")
