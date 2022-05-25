#Ejercicio 18 F
#Definir una función que tome un entero n y devuelva los primeros n primos.


def primo(numero):
    if numero<2:
        return False
    for i in range(2,numero//2+1):
        if numero%i==0:
            return False
    return True

def primoCercano(n1):
    encotrado=False
    i=n1+1
    while encotrado==False:
        if primo(i)==True:
            encotrado=True
            return i
        i=i+1
n=24
print  (primoCercano(n))