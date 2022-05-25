# LISTAS DE LISTAS:

productos=[["abel",40],["cielo",11],["ludmila",12],["aaa",50]]

for producto in productos:#RECORRE POR ELEMENTO
    print(producto)# Imprime cada uno de los elementos que estan dentro de la lista.

for i in range(len(productos)):#RECORRO POR POSICION PARA ACCEDER A LOS ELEMENTOS DE LAS SUB_LISTAS.
    if productos[i][1]>30:
        print(productos[i])
         #ACCEDO A LA POSICION 1 DEL SUB_LISTADO


for i in range(len(productos)):
    if productos[i][0][0]=="a":#ACCEDO AL SUB_LISTADO POSICION 0 ="ABEL" Y ACCEDO A LA POSICION 0 ="A"
        print(productos[i])
