a = [30, 4, 50, 6, 70,9, 8, 90, 10]
b = [4, 6, 7, 8, 10,9, 12, 14, 16]

def par (numero):
    if numero%2==0:
        return True
    else:
        return False

def interseccione(lista,lista2):
    nueva=[]
    for i in range(len(lista)):
        for j in range(len(lista2)):
            if lista[i]==lista2[j] and par(lista[i])==True:
                nueva.append(lista2[j])
    return nueva

def productoIntersecciones(lista):
    productos=[]
    unicos=[]
    for i in range(len(lista)):
        for j in range(len(lista)-1,-1,-1):
            productos.append((lista[i])*(lista[j]))
            i=i+1
        for elemento in productos:
            if elemento==elemento:
                productos.remove(elemento)
            return productos

def extremos(lista):
    extremos=[]
    mayor=lista[0]
    menor=lista[-1]
    extremos.append(mayor)
    extremos.append(menor)
    return extremos

nueva=interseccione(a,b)
nueva=productoIntersecciones(nueva)
nueva=extremos(nueva)
print(nueva)

