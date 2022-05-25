#Ejercicio 18 F â™£
#Una funcionn cuadratica se escribe como ax2+bx+c. La misma puede tener una, dos o ninguna
#raaiz. Escribir un programa que pida al usuario los datos de la misma, es decir, a, b y c, y muestre
#todas sus raaices, o el mensaje No tiene raaicces cuando corresponda. Recordar que las raaices estann
#dadas por la forrmula
# âˆ’b Â±âˆšb2 âˆ’ 4ac
#       2a


import math
print("Este programa calcula ax^2 + bx + c = 0")

a = float(input("Ingrese el valor de a"))
b = float(input("Ingrese el valor de b"))
c = float(input("Ingrese el valor de c"))

if(a != 0):

    discriminante = b*b - 4*a*c

    #precondicion a != 0
    if(discriminante > 0):
        x1 = (-b + math.sqrt(discriminante))/(2*a)
        x2 = (-b - math.sqrt(discriminante))/(2*a)
        print("Las soluciones son: ", x1, " y ", x2)
    else:
        if(discriminante==0):
            x1 = -b/(2*a)
            print("La solucion es: ", x1)
        #caso discriminante < 0
        else:
            print("La ecuacion no tiene solucion")

else:

    #tarea para el hogar :-)





