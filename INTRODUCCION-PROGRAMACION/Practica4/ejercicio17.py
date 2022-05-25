#Ejercicio 17 F
#Escribir una funciÃ³n (y probarla en un programa) para cada una de las siguientes descripciones:
#a) una funciÃ³n que se llame tieneRepetidas que tome una cadena como parÃ¡metro y
#devuelva True si esa cadena tiene alguna letra que aparece mÃ¡s de una vez y False
#en caso contrario.
#b) una funciÃ³n que se llame aparece que tome dos parÃ¡metros, una letra y una cadena,
#y devuelva True si la letra aparece en la cadena y False en caso contrario.
#c) una funciÃ³n que se llame dameRepetida que tome una cadena como parÃ¡metro y
#retorne la primer letra que aparece repetida en la cadena
#d) una funciÃ³n que se llame quitarRepeticiones que tome dos parÃ¡metros, una
#cadena y una letra, y devuelva otra cadena igual a la anterior pero sin las
#repeticiones de esa letra. Por ejemplo, un programa que llame a la funciÃ³n
#asÃ­: quitarRepeticiones("mate cocido", "c"), deberÃ¡ retornar la cadena "mate
#coido".

#a
def tieneRepetidas(cadena,letra):
    cont=0
    for char in cadena:
        if char==letra:
            cont=cont+1
    if cont >=2:
        return True
    else:
        return False
#b
def aparece (cadena,letra):
    for char in cadena:
        if char==letra:
            return True
    else:
        return False

#c
def dameRepetidas(cadena):
    letrarepetida=[]
    for char in cadena:
        if tieneRepetidas(cadena,char)==True and aparece(cadena,char)==True:
            letrarepetida.append(char)
    print(letrarepetida[0])

dameRepetidas("cbalabbbrc")







