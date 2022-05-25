#c) Hacer una funcion que determine si un numero ingresado por el usuario es un numero
#abundante. Numero abundante: todo numero natural que cumple que la suma de sus
#divisores propios es mayor que el propio numero. Por ejemplo, 12 es abundante ya
#que sus divisores son 1, 2, 3, 4 y 6 y se cumple que 1+2+3+4+6=16, que es mayor
#al propio 12.

def abundante(numero):
    suma=1
    for i in range(2,numero):
        if numero %i==0:
            suma=suma+i
    if suma >= numero:
        return  numero,"es abundante"
    else:
        return numero, "no es abundante"


n=int(input(""))
print (abundante(n))







