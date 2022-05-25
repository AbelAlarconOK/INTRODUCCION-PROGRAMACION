#Ejercicio 28
#Escribir un programa que pida al usuario una cadena y una letra y reemplace las apariciones
#de dicha letra por asteriscos. Por ejemplo, si el usuario ingresa:
#"programador"
#"r"
#el programa debe devolver "p * og * amado *"


palabra=input("ingrese una letra: ")
letra=input("ingrese una letra: ")

letra_nueva=letra.lower()
palabra_nueva=palabra.lower()

nueva_palabra=""
for char in palabra:
    if char==letra:
        nueva_palabra=nueva_palabra+("*")
    else:
        nueva_palabra=nueva_palabra+char

print(nueva_palabra)

