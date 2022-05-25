#·Escribir un programa que reciba una
#cadena, verifique si coincide con “Ana”
#e, independientemente de la
#comparación anterior, valide si la
#cantidad de caracteres presentes es
#múltiplo de 3. En todos los casos,
#debe imprimir mensajes adecuados.


cadena=input("ingrese cadena")

if cadena=="ana":
    print("se ingreso {} ".format("ana"))
else:
    print("se ingreso una cadena distinta que  {} ".format("ana"))

le_catn_caract=len(cadena)%3==0

if le_catn_caract:
    print("es multiplo")
else:
    print("no es multiplo")

