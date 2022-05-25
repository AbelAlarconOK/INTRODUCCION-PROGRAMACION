#Ejercicio 25 F
#Hacer una programa que, dada una palabra, la escriba recuadrada por asteriscos. Por ejemplo,
#si la palabra es "Ganaste", el programa debería escribir:
#***********
#* Ganaste *
#***********

palabra=input("ingrese una palabra")

palabranueva=len(palabra)
ast=""
for i in range(1,palabranueva+5):
    ast=ast+"*"
print(ast+"\n*",palabra,"*\n"+ast)
