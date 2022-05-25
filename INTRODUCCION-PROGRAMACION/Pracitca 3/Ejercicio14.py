#Ejercicio 14 F
#El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
#ln(2) = 1 -1/2+1/3-1/4+1/5


n=int(input("ingrese cantidad de terminos: "))

suma=1

for i in range(1,n+1):
    suma=suma+((-1)**i/(i+1))

print(suma)
