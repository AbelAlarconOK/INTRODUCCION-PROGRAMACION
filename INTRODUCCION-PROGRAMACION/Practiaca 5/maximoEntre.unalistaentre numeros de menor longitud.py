#Ejercicio 11 F
#Escribir una funciÃ³n llamada maximoEntre que tome una lista de nÃºmeros y dos enteros a y b
#menores que la longitud de la lista y devuelva el Ã­ndice del mÃ¡ximo elemento considerando solo
#los que estÃ¡n entre el Ã­ndice a y el Ã­ndice b.



#funcion

def maximoEntre(n1,n2,lista):
    nueva=[]
    for i in range(numero1,numero2+1):
        nueva.append(lista_numeros[i])


    mayor=nueva[0]
    indice=0

    for j in range(len(nueva)):
        if nueva[j]>mayor:
            mayor=nueva[j]
            indice=j
    return indice

#programa principal
lista_numeros=[50,10,70,80,20,30,50,15,3,120]
numero1=4
numero2=9

print (maximoEntre(numero1,numero2,lista_numeros))
