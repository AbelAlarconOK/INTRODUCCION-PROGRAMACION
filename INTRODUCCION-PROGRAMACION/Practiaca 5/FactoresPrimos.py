#Ejercicio 19 F
#Definir una función que tome un entero n y devuelva la lista de los primos que aparecen al
#factorear n. Ejemplo, para 24, la lista debe ser: [2, 2, 2, 3]

def primo(n):
    for j in range(2,n//2+1):
        if n%j==0:
            return False
    return True


def factores (n):
    lista = []
    i = 2
    while i <= n:
        if (n% i == 0 and  primo (i)):
            lista.append (i)
            n = n / i
        else:
            i =  + 1
    return lista

print (factores (24))
