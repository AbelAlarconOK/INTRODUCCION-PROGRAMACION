#Ejercicio 13
#Hacer una funciÃ³n que indique si un nÃºmero es Libre de Cuadrados: NÃºmero libre de cuadrados:
#todo nÃºmero natural que cumple que en su descomposiciÃ³n en factores primos no aparece ningÃºn
#factor repetido. Por ejemplo, el nÃºmero 30 es un nÃºmero libre de cuadrados.

def facotrPrimo(n):
    bandera=True
    for i in range(2,n//2+1):
        if(n%i==0):
            bandera=False
    return bandera


a=int(input("Ingrese un numero"))
producto=1
for i in range(1,a+1):
    if(a%i==0 and primo(i)):
        producto=producto*i;

if(producto==a):
    print(a,"SI es libre de cuadrados")
else:
    print(a,"NO es libre de cuadrados")