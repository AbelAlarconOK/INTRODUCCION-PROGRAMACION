#Ejercicio 17 F â™£
#Escribe un programa que pida los coeficientes de una ecuacion de primer grado (ax + b = 0)
#y escriba la solucion. Recuerda que una ecuacipn de primer grado puede no tener solucion, tener
#una solucion unica, o que todos los numeros reales sean solucion.



print("Este programa calcula ax + b  = 0")

a = float(input("Ingrese el valor de a"))
b = float(input("Ingrese el valor de b"))

if(a==0 and b==0):
    print("todos los reales")
else:
    if(not a):
        print("no tiene solucion")
    else:
        print("x vale:",(-b)/a)
