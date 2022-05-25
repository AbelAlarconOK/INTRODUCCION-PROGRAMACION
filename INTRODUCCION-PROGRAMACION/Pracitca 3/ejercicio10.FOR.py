#Hacer un progranme que permita al usuario elegir un numero positivo n y luego muestre
#en pantalla el preducto ( es decir la multiplicaion) de los numeros entre 1 y n.

n=int(input("ingrese un numero: "))

factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)