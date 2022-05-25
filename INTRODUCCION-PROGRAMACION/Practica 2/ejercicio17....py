#Ejercicio 17 F â™£
#Escribe un programa que pida los coeficientes de una ecuacion de primer grado (ax + b = 0)
#y escriba la solucion. Recuerda que una ecuacipn de primer grado puede no tener solucion, tener
#una solucion unica, o que todos los numeros reales sean solucion.

a=int(input("ingrese un primer valor: "))
b=int(input("ingrese un segundo valor: "))

if a !=0:
    print("la solucion es: x = ", -b/a)
else:
    if(b==0):
        print("existen infinitos soluciones.")
    else:
        print("no hay soluciones para la ecuacion planteada."2)