#Ejercicio 19 ÃƒÂ¢Ã¢â€žÂ¢Ã‚Â£
#a) Escribir un programa que permita al usuario elegir un nÃƒÆ’Ã‚Âºmero m y un n y muestre
#todos los pares de numeros que se pueden formar con los nÃƒÆ’Ã‚Âºmeros que estÃƒÆ’Ã‚Â¡n entre
#ellos, pero esta vez que lo haga sin repetir inversos. Por ej. si el usuario ingresara 4
#y 6, el programa deberÃƒÆ’Ã‚Â¡ mostrar
#4 4
#4 5
#4 6
#5 5
#5 6
#6 6
#b) Cambiar el programa para que use sÃƒÆ’Ã‚Â³lo un ciclo en vez de dos.

m=int(input(""))
n=int(input(""))

for i in range(m,n+1):
    for j in range(m,n+1):
        print(i,j)
    m=m+1


for i in range(m,n+1):
    for j in range(i,n+1):
        print(i,j)



i=m
j=m

while (j<=n and i <=n):
    pint(i,j)
    j=j+1
    if j==n+1:
        j=i
        i=i+1
