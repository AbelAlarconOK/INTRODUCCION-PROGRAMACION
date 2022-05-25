#Ejercicio 22 F
#Escribir un programa que pida al usuario una cadena, y luego escriba en pantalla la cantidad
#de veces que aparece cada letra (sin mostrar las que no aparecen). Ej:
#Palabra ingresada: "conocido"
#c : 2
#o : 3
#n : 1
#i : 1
#d : 1

def cantApariciones(letra, cadena):
    cant=0
    for i in range(len(cadena)):
        if (letra==cadena[i]):
            cant+=1
    return (cant)


def imprimeCantApariciones(cadena):
    listaAparecidos=[]
    for i in range(len(cadena)):
        letra=cadena[i]
        if (cantApariciones(letra,listaAparecidos)==0):
            listaAparecidos.append(letra)
            print (letra, ": ", cantApariciones(letra,cadena))




palabra=input("Ingrese una palabra")
print(palabra)

imprimeCantApariciones(palabra)