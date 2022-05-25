#Ejercicio 16
#El propósito de este ejercicio es tomar el código de un ejercicio anterior y encapsular una
#parte de él en un función que toma parámetros. Partiendo de la resolución del ejercicio 25 de la
#práctica de ciclos y cadenas,
#a) escribir una función que tome como parámetros una cadena y una letra, y retorne
#la cantidad de veces que aparece esa letra en esa cadena.
#b) probarla para asegurarse que funciona bien.
#c) transformar el código del ejercicio 25 para que utilice la nueva función.



def repetida(cadena,letra):
    cont=0
    for i in cadena:
        if (i==letra):
            cont+=1
    print (letra, "aparece en ",palabra, cont, "veces")


palabra=input("")
letra=input("")
repetida(palabra,letra)

