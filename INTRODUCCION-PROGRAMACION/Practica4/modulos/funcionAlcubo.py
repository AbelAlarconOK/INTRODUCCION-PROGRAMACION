#Ejercicio 7 F
#a) Escribir una funciÃ³n que se llame elevarAlCubo que tome un nÃºmero y retorne el
#valor de ese nÃºmero al cubo.
#b) Guardar el ejercicio anterior en un archivo llamado funcionCubo.py
#c) Correr el siguiente cÃ³digo en un archivo nuevo y chequear que los resultados sean
#correctos:
#print(0, "al cubo:", elevarAlCubo(0))
#print(1, "al cubo:", elevarAlCubo(1))
#print(2, "al cubo:", elevarAlCubo(2))
#print(3, "al cubo:", elevarAlCubo(3))
#print(4, "al cubo:", elevarAlCubo(4))
#print(5, "al cubo:", elevarAlCubo(5))
#print(6, "al cubo:", elevarAlCubo(6))
#print(-1, "al cubo:", elevarAlCubo(-1))
#print(-2, "al cubo:", elevarAlCubo(-2))
#print(-3, "al cubo:", elevarAlCubo(-3))
#print(-4, "al cubo:", elevarAlCubo(-4))
#print(-5, "al cubo:", elevarAlCubo(-5))


def elevarAlcubo(numero):
    return numero**3

n=int(input(""))
print(n, "al cubo =",elevarAlcubo(n))