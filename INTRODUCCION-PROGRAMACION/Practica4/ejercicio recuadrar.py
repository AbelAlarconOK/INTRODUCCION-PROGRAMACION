#ejercicio sobrevivir.

def recuadrar(palabra):
    asteriscos_dinamicos=""
    for i in range(len(palabra)):
        asteriscos_dinamicos=asteriscos_dinamicos+"*"
    fila_ast="**"+asteriscos_dinamicos+"**\n"
    fila_medio="*"+" "+palabra+" "+"*\n"

    print(fila_ast + fila_medio + fila_ast)

recuadrar("abel")
