#c) Hacer un programa que permita al usuario elegir un nÃºmero n y un nÃºmero c, y
#luego muestre los c nÃºmeros naturales que le siguen a n (n + 1, n + 2, Â· Â· Â· , n + c).


n=int(input("Ingrese un numero: "))
c=int(input("ingrese otro numero: "))
i=n
while i <=n+c:
    print(i)
    i=i+1

