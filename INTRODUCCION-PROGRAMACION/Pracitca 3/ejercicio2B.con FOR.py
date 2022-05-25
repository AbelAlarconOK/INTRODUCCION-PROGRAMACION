#b) Hacer un programa que permita al usuario elegir un nUmero m y un n y luego
#muestre todos los naturales entre m y n (m, m + 1, m + 2, Ã‚· Ã‚Â· Ã‚Â· , n -1, n). Ã‚Â¿QuE pasa
#si n es menor que m?

n=int(input("ingrese un numero: "))
m=int(input("ingrese otro numero: "))

for n in range(n, m-1,-1):
    print(n)