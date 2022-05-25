#Ejercicio 1 F
#Hacer un programa que guarde la siguiente lista en una variable: ["elefante", "jirafa",
#"mono"], luego pida el nombre de otro animal, lo agregue a la lista e imprima en pantalla el
#cuarto animal de la lista.


animales=["elefante","jirafa","mono"]


n=input("Ingrese un animal: ")
animales.append(n)
print (animales[3])