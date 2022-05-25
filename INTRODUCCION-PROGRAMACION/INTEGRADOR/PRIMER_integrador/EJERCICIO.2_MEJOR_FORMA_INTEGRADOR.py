listaCodigos=[111, 112, 113, 114, 115, 116]
listaMarcas=["Cocinera","Morirse","Ayudin","La Serena","Top Casa","Cola Cola"]
listaTipos=["Aceites","Harinas","Limpieza","Lacteos","Electro","Gaseosas"]
listaPrecios=[150, 90, 120, 80, 440, 135]

informe=[]

def Aparece(enteros,blanco):
    for n in range (len(enteros)):
        if (enteros[n] ==blanco):
            return n
    return False

def informe_Final(lista):
    if Aparece(listaCodigos,ingreso_codigo)==False:
        return -1
    informe=[]
    precio_final=0
    precio=0
    descuento=0

    informe.append(listaCodigos[i])
    informe.append(listaMarcas[i])
    informe.append(listaTipos[i])
    precio=listaPrecios[i]
    descuento=precio*0.10
    precio_final=precio-descuento
    informe.append(precio_final)

    return informe

ingreso_codigo=int(input("ingrese un codigo de producto:"))
i=Aparece(listaCodigos,ingreso_codigo)
print(informe_Final(informe))