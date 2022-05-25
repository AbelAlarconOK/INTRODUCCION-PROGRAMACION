#Hacer una función que dado dos números enteros indique, en caso de existir,
#el divisor no primo mayor de ambos. Por ejemplo: Entre 60 y 80 la función debe devolver el número 20. Se podrán desarrollar funciones auxiliares.

def primo(numero):
    if numero<2:
        return False
    for i in range(2,numero):
        if numero%i==0:
            return False
    return True


#mejor forma.
def primoMasCercano(n1,n2):
    i=1
    primos=[0]
    mayor=primos[0]
    encontrado=False
    while  i<=n1+1:
        if primo(i)==False:
            encontrado=True
        if n2%i==0 and n1%i==0:
            primos.append(i)
        i=i+1
    for j in range(len(primos)):
        if primos[j]>mayor:
            mayor=primos[j]
    return mayor

print(primoMasCercano(60,80))