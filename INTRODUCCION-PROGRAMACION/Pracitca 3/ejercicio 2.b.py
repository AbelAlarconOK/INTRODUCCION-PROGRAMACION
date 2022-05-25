#b) Hacer un programa que permita al usuario elegir un nÃºmero m y un n y luego
#muestre todos los naturales entre m y n (m, m + 1, m + 2, Â· Â· Â· , n âˆ’ 1, n). Â¿QuÃ© pasa
#si n es menor que m?


n=int(input("ingrese un numero: "))
m=int(input("igrese otro numero: "))
i=m
while i<=n:
    print(i)
    i=i+1