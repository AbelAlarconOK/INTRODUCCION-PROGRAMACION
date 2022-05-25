#Ejercicio 17
#EJERCICIO:17
#a) Hacer un programa que permita al usuario elegir un nÃƒÂºmero m y un n y muestre
#pares de numeros complementarios, o sea (m, n)(m + 1, n Ã¢Ë†â€™ 1)(m + 2, n Ã¢Ë†â€™ 2). . .(n Ã¢Ë†â€™
#1, m + 1)(n, m). Por ejemplo, el usuario ingresa 5 y 10, 5 serÃƒÂ¡ el complementario de
#10, 6 el de 9 y 7 el de 8, y deberÃƒÂ¡ mostrarse:
#5 10
#6 9
#7 8
#8 7
#9 6
#10 5
#b)hacer que el programa se detengas cuando m es mas grande que n.

m=int(input(""))
n=int(input(""))


print(m,n)
for i in range (m+1,n+1):

    n=n-1
    print(i,n)



m=int(input(""))
n=int(input(""))

i=m
while m <=n:
    print(m,n)
    m=m+1
    n=n-1






