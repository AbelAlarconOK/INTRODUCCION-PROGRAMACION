#c) Hacer un programa que permita al usuario elegir un nÃºmero n y un nÃºmero c, y
#luego muestre los c nÃºmeros naturales que le siguen a n (n + 1, n + 2, Â· Â· Â· , n + c).

n=int(input("Ingrese un numero: "))
c=int(input("ingrese otro numero: "))

for n in range (n,(n+c)+1,1):
    print(n)