#f) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
#muestre en pantalla los últimos c divisores de n.


c=int(input("ingrese un valor para n: "))
n=int(input("ingrese un valor para c: "))

x=n
a=1
while a<=c:
    if n%x==0:
        a=a+1
        print(x)
    x=x-1