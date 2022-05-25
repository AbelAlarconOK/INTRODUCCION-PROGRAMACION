#Ejercicio 16 F
#Un añoo es bisiesto si es multiplo de 4. Pero no siempre, las excepciones son los aaños mulltiplos
#de 100 que no son mulltiplos de 400 (1900 no es bisiesto pero 2000, si­). Escribir en papel un
#programa que diga si un añoo ingresado por el usuario es bisiesto, realizar varias pruebas de
#escritorio, luego pasarlo a Python y vericar los resutlados.


año=int(input("ingrese el aÃ±o: "))

if año % 4 == 0:
       if(año % 100 == 0 and año % 400 != 0):
        print("el anio", año, "No es bisiesto")
       else:
        print("el anio", año, "Es bisiesto")
else:
       print("el anio", año, "No es bisiesto")