#e) Hacer un programa que permita al usuario elegir dos nÃºmeros positivos c y n y luego
#muestre en pantalla los primeros c divisores de n.

c=int(input("Ingrese un numero positivo para c: "))
n=int(input("Ingrese un numero positivo para n: "))

contador=0
for i in range(1,n+1):
    if n%i==0 and c!=contador:
        contador=contador+1#contador para cortar cuando llegue a el valor de c.
        print(i)
