# Ejercicio 18 F Ã¢â„¢Â£
#a) Escribir un programa que permita al usuario elegir un nÃƒÂºmero m y un n y muestre
#todos los pares de numeros que se pueden formar con los nÃƒÂºmeros que estÃƒÂ¡n entre
#ellos. Por ej. si el usuario ingresara 4 y 6, el programa deberÃƒÂ¡ mostrar
#4 4
#4 5
#4 6
#5 4
#5 5
#5 6
#6 4
#6 5
#6 6
#b) Cambiar el programa para que use sÃƒÂ³lo un ciclo en vez de dos.


m=int(input(""))
n=int(input(""))

#for i in range(m,n+1):constante
#    for j in range(m,n+1):variable
#        print(i,j)

k=m
i=m

while (m<=n):
    print(m,i)
    i=i+1
    if i>n:
        m=m+1
        i=k

