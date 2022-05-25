#Ejercicio 19 F
#Escribir en Python un programa que pida al usuario que ingrese dos valores y
#los guarde en dosvariables, x e y. El programa deberá intercambiar los valores
# de x e y y luego mostrar en pantalla:
#El valor de x es: <x>El valor de y es:<y>
#donde en lugar de <x> e <y> deberá mostrarse el valor de las respectivas
#variables.

x=10
y=8

print( "el valor de x es:", x , "y el valor de y es:" , y)

aux = x = y
y = x

print("el valor de x es: ",x, "Y el valor dey es: ", y )