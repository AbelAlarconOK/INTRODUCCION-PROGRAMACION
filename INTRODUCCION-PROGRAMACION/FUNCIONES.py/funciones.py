import math

def CalculadoraAreaCirculo (radio):
    return math.pi*radio**2

r=int(input("radio:"))
valor=CalculadoraAreaCirculo(r)
print(valor).