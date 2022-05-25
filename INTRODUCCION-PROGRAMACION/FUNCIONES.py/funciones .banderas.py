
#FUNCIONES Y BANDERAS:
def primo(m):
    i=2#jamas 0 paranimero primos.
    #cont_div=0
    bandera=True
    while (i<m and bandera==True):
        if m%i==0:#true, aumentamos contador.
            bandera=False
        i=i+1
    return bandera

#programa principal.
n=int(input(""))
b=primo(n)

if (b==True):
    print(n,"primo")
else:
    print(n,"no es primo")