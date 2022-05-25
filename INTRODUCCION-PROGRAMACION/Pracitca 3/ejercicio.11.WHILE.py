#Ejercicio 11
#Hacer un programa que reciba un numero m y determine el primer n para el cual la suma
#1+2+...+n > m. Por ejemplo, si el usuario ingresa 11 se deberaÂ¡ retornar 5 ya que 1+2+3+4 =
#10 < 11 y 1 + 2 + 3 + 4 + 5 = 15 > 11.

m=int(input("ingrese un numero para m: "))
i=1
suma=0#la suma de los numeros.
n=1
while i<=m:
    suma=suma+i#la suma incrementa de valor,mientras se cumpla la condicion de I.
    if suma <=m:#la suma de los valores no debe superar el numero ingresado.
        n=n+1#al valor n comienza a sumar si la condicion de la suma es menor a , M.
    i=i+1
print(n)


#es decir cuando la suma se menor o igual a m=(11)=1+2+3+4=10.
#n va a aumentar hasta el numero 4 ya que es donde corta la condicion.
