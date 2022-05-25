#Ejercicio 12
#Un profesor clasifica las notas de sus alumnos de la siguiente manera:
#1-3 Reprobado
#4-6 Debe rendir examen final
#7-10 Eximido
#a) Escribir un programa que indique la clasificación de una nota.
#b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasicación
#del mismo.


n1=int(input("nota"))

if n1 >= 7 :
    print("eximido")
else:
    if n1<= 3 :
        print (" reprobado")
    else:
        print("debe rendir final")


n1=int(input("primer nota"))
n2=int(input("segunda nota"))
n3=int(input("tercer nota"))
promedio=(n1+n2+n3)/3

if n1 >= 7 :
    print("eximido")
else:
    if n1<= 3 :
        print (" reprobado")
    else:
        print("debe rendir final")





