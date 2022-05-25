#Ejercicio 27
#Escribir un programa que pida al usuario una cadena e indique si esta posee un diptongo (dos
#vocales unidas).

palabra="aeto"

tiene=False
nueva=""
for char in palabra:
    if char =="a" or char=="e"or char=="i" or char=="o" or char=="U":
        nueva=nueva+char
        if len(nueva)>=2:
            tiene=True
    if tiene==True:
        print("tiene")
    else:
        print("no tiene")
