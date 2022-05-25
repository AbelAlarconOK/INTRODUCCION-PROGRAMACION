#teniendno en cuenta la ecuacion de primet grado ax^2+bx+c=0.ecuacion de primer grado tienen un resultado.
#formula de ecuacion de segundo grado x= -b +-raiz cuadrada de = b^2-4*a*c dividido 2*a
#raiz cuadrada negativa= no hay soluciones.
#raiz cuadrdada positiva=tenemos soluciones para la ecuacion.

import math#libreria de phyton

a = int(input("Ingrese el coeficiente del termino cuadratico"))
b = int(input("Ingrese el coeficiente del termino lineal"))
c = int(input("Ingese un valor para la ordenada al origen"))
#calcular discriminante= numero de adentro de la raiz cuadrada.(si la raiz cuandrada es positia o negaiva).

discriminante=b**2-4*a*c

#comprobamos y calculamos.

if discriminante < 0: #no hay raices reales.
   print ("no hay raices")
else:
    if discriminante== 0:#es unica raiz.
     x = -b/(2*a)
     print ("la solucion es unica en x = ",x)
    else:#(math.sqrt)para resolver raiz cuadrada.
     x1 = (-b + math.sqrt(discriminante))/(2*a)#ecuaciones de segunda grado tienen 2 resultados
     x2 = (-b - math.sqrt(discriminante))/(2*a)
     print("existen dos soluciones distintas en: x1 = ", x1, "y x2 = ", x2)

