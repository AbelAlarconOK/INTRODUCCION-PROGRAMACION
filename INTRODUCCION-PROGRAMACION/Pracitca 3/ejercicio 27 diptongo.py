#Ejercicio 27
#Escribir un programa que pida al usuario una cadena e indique si esta posee un diptongo (dos
#vocales unidas).

v1="aereo"
cont=0

for i in v1:
    if i in ("a","e","i","o","u"):
        #print(i,end="")
        cont=cont+1
        if cont==2:
            print("dipotongo")
    else:
        cont=0


