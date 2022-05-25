#usar funcines:

#escribir una funcion que reciba un natural n y devuelva una cadena conformada
#por una linea de asteriscos horizontales.
#ej2 n=8 , salida de funcioines :********


#funciones:

def astericos(n,simbolo):
    nueva_cadena=""

    for i in range(n):
        nueva_cadena=nueva_cadena+simbolo

    return nueva_cadena

#programa principal.

n=int(input("ingrese cantida de numeros"))
simbolo=input("ingrese un caracter")
cadena=astericos(n,simbolo)
print(cadena)

