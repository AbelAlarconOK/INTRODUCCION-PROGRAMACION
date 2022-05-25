#Ejercicio 11
#Hacer un programa que reciba un numero m y determine el primer n para el cual la suma
#1+2+...+n > m. Por ejemplo, si el usuario ingresa 11 se deberaÂ¡ retornar 5 ya que 1+2+3+4 =
#10 < 11 y 1 + 2 + 3 + 4 + 5 = 15 > 11.
m=int(input("ingrese un numero para m: "))
i=1
suma=0#la suma de los numeros.
n=1
for i in range(1,m+1,1):
    suma=suma+i
    if suma <=m:
        n=n+1
print(n)