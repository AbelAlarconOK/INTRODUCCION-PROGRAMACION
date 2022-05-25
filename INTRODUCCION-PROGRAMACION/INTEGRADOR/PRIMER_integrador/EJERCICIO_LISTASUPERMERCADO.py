ids = ['144', '145', '146']
producto = ['Mortadela 100gr', 'Salamín 100gr', 'Queso 150gr']
precio = [250, 300, 280]
cantidad_disponible = [5, 8, 10]
informe=[]

def Aparece(enteros,blanco):
    for n in range (len(enteros)):
        if (enteros[n] ==blanco):
            return n

    return False
def dondeAparece(lista,n):
    for h in range(len(lista)):
        if lista[h] ==n:
            return True
        else:
            return False

def informe_Final(lista):
    if dondeAparece(ids,ingreso_codigo)==False:
        return -1
    informe=[]
    precio_final=0
    valor=0
    descuento=0
    if cantidad>cantidad_disponible[i]:
        print("no,disponible")
        print("La cantidad disponible es: ",cantidad_disponible[i])

    informe.append(ids[i])
    informe.append(producto[i])
    valor=precio[i]*cantidad
    descuento=valor*0.10
    precio_final=valor-descuento
    informe.append(precio_final)

    return informe

ingreso_codigo=input("ingrese un codigo de producto: ")
cantidad=int(input("ingrese cantida: "))
i=Aparece(ids,ingreso_codigo)
i=int(i)
print(informe_Final(informe))