#hace una funcion que calcule el maximo entre 3 valores(a,b,c).

def max(a,b):
    if a>b:
        return a
    return b

def maximo(a,b,c,):
    return max(max(a,b),c)

print(maximo(1,2,3))