#Ejercicio 6 F
#Definir una funcion que tome una lista y devuelva True si tiene al menos un elemento repetido,
#y False en caso contrario-


numeros =[1,2,3,4,5,6]
repetido=[]
archivo=[]
def rePetido(lista):
    for n in lista:
        if n not in archivo:
              archivo.append(n)
        else:
            repetido.append(n)
    if len(repetido)>=1:
        return True
    else:
        return False


print (rePetido(numeros))


