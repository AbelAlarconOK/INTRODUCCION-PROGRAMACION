#b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
#5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).

n=int(input("ingrese un numero: "))

i=n
while i<=n+5:
    print(i)
    i=i+1