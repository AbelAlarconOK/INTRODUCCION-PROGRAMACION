#4- Hacer una funcion que reciba una lista y devuelva
#otra solo con los elementos sin repeticiones.

comida=["helado","caramelo",2,2,1,"chupetin","caramelo","sopa","chupetin"]


#def sinRepetir(lista):
#    conjunto=set(lista)
#    lista=list(conjunto)
#    return lista

#print (sinRepetir(comida))


unicos=[]
nueva_lista=list(comida)

for char in nueva_lista:
    if char not in unicos:
        unicos.append(char)
    else:
        comida.remove(char)

print(comida)
