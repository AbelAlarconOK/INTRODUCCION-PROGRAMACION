#Hacer un progranme que permita al usuario elegir un numero positivo n y luego muestre
#en pantalla el preducto ( es decir la multiplicaion) de los numeros entre 1 y n.

n=int(input("ingrese un numero: "))

i=1
factorial=1
while i <= n:
    factorial=factorial*i
    i=i+1
print(factorial)


