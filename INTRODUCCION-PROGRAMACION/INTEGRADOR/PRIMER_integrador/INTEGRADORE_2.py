listaCodigos=[111, 112, 113, 114, 115, 116]
listaMarcas=["Cocinera","Morirse","Ayudin","La Serena","Top Casa","Cola Cola"]
listaTipos=["Aceites","Harinas","Limpieza","Lacteos","Electro","Gaseosas"]
listaPrecios=[150, 90, 120, 80, 440, 135]

def Aparece(enteros,blanco):
    for n in range (len(enteros)):
        if (enteros[n] ==blanco):
            return True
    return False
def dondeAparece(lista,n):
    elemento=[]
    for h in range(len(lista)):
        if h ==n:
            elemento=lista[h]
    return elemento


def informe (codigo):
    if Aparece(listaCodigos,codigo)==False:
        return -1
    informe_final=[]
    descuento=0
    indice=0
    precio=0
    precio_final=0
    marcas=""
    tipo=""
    for i in range(len(listaCodigos)):
        if listaCodigos[i]==codigo:
            indice=i
            informe_final.append(codigo)

    for j in range(len(listaMarcas)):
        if indice ==j:
            marcas=listaMarcas[j]
            informe_final.append(marcas)

    for n in range(len(listaTipos)):
        if indice==n:
            tipo=listaTipos[n]
            informe_final.append(tipo)

    for s in range(len(listaPrecios)):
        if indice==s:
            precio=listaPrecios[s]
            descuento=precio*0.10
            precio_final=precio-descuento
            informe_final.append(precio_final)

    return informe_final

n=int(input("ingrese un codigo"))
print (informe(n))
