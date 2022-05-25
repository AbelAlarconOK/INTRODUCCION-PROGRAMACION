#Ejercicio 14 F
#El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
#ln(2) = 1 −1/2+1/3−1/4+1/5

n=int(input("ingrese un numero para la cantidad de terminos del logaritmo: "))


ln=0

for deno in range (1,n+1):
    if deno%2==0:
        deno=deno*(-1)
    ln=ln+1/deno
print(ln)

import math
print (math.log(2)
