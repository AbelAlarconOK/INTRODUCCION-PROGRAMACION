#ejercicio26.

#Hacer un programa que dada una palabra y una letra, imprima la cantidad de
# apariciones de esa letra.


palabra=input("ingrese ua palabra: ")
letra=input("ingrese una palabra: ")

contador_aparicicones=0

for char in palabra:
    if char==letra:
        contador_aparicicones=contador_aparicicones+1

print("la palabra tiene", palabra,"tiene repetida a letra",
letra, "un total de ",contador_aparicicones,"veces")
