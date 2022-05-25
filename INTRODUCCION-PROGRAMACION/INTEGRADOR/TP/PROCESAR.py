def procesar(lista,candidata,listaIzq,listaMed,listaDer):
    puntaje=0
    for i in range(len(lista)):
        if lista[i]==candidata and esValida(lista,candidata,listaIzq,listaMed,listaDer)==True:
            puntaje=puntos(candidata)
            return puntaje
    else:
        return puntaje