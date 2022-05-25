#Ejercicio 15 F â™£
#Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
#El programa deberÃ¡ luego hacer que en la variable a quede el menor de los valores recibidos, en
#b el intermedio y en c el mayor (es decir, ordenarÃ¡ los valores).

a=int(input("ingrese a"))
b=int(input("ingrese b"))
c=int(input("ingrese c"))
#a es el menor
if(a<b and a<c):

    if(b>c):
        #menor=a
        #medio=b
        #meyor=c
        #menor=a
        aux=b
        b=c
        c=aux
        #medio=c
        #mayor=b
else:#b es el menor
    if(b<a and b<c):

        if(a<c):
            aux=a
            a=b
            b=aux
            #menor=b
            #medio=a
            #mayor=c
        else:
            aux=b
            b=c
            c=a
            a=aux
            #menor=b
            #medio=c
            #mayor=a
    else:#c es menor

          if(a<b):
            aux=c
            c=b
            b=a
            a=aux
             #menor=c
             #medio=a
             #mayor=b
          else:
            aux=a
            a=c
            c=aux
             #menor=c
             #medio=b
             #mayor=a
print(a,b,c)