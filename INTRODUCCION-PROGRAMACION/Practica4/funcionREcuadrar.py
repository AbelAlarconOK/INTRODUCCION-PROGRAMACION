#Ejercicio 15
#Hacer una función (no pura) que reciba una palabra y la imprima recuadrada por asteriscos.
#Por ejemplo si la cadena fuera sobrevivir, la función debería imprimir
#**************
#* sobrevivir *
#**************


def recuadrar(palabra):
    asteriscos_dinamicos=""
    for i in range(len(palabra)):
        asteriscos_dinamicos=asteriscos_dinamicos+"*"
    fila_ast="**"+asteriscos_dinamicos+"**\n"
    fila_medio="*"+" "+palabra+" "+"*\n"

    print(fila_ast + fila_medio + fila_ast)

recuadrar("abel")
