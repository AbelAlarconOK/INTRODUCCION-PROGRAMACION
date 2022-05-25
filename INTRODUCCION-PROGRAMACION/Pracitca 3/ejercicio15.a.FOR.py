#Ejercicio 15 F
#El número 1/4π se puede aproximar de la siguiente manera:14π = 1 −1/3+1/5−1/7+1/9
#−1/11+1/13−1/15
#a) Escribir un programa que le pregunte al usuario la cantidad de término a sumar
# y muestre la aproximacion de pi con esa cantidad de terrminos.


print ("Calcularemos PI")
n=int(input("Ingrese la cantidad de terminos"))
suma = 0
signo = 1
for i in range(1,n+1,2): # 1,3,5,...,n
    suma = suma + 1/i * signo
    signo=-signo
print(4*suma)



import math
print ("Calcularemos PI")
epsilon=0.000001
suma = 0
signo = 1
i=1
pi=math.pi
while(abs(4*suma-pi)>epsilon):
    suma = suma + 1/i * signo
    signo=-signo
    i=i+2
print(4*suma)