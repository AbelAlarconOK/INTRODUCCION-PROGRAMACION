#Parte 2 Cadenas
#Ejercicio 23
#a) Escribir un programa que pida al usuario un nÃƒÂºmero n y muestre una lÃƒÂ­nea de n
#asteriscos. Ejemplo, para n = 8, el programa deberÃƒÂ¡ mostrar:
#********


#n=int(input(""))


#i=0
#char=""
#while i <=n:
#    char=char+"*"
#    i=i+1
#print(char)

#b) Escribir un programa que pida al usuario un nÃºmero n y muestre n lÃ­neas de
#1, 2, 3, ...n asteriscos respectivamente. Ejemplo, para n = 5, el programa deberÃ¡
#mostrar:
#*
#**
#***
#****
#*****

#m=int(input(""))

#asteriscos=""

#for i in range(m+1):
#    asteriscos=asteriscos+"*"
#    print(asteriscos)


#c) Escribir un programa que pida al usuario un nÃºmero n y muestre n lÃ­neas de 2n âˆ’ 1
#asteriscos respectivamente. Ejemplo, para n = 5, el programa deberÃ¡ mostrar:
#*
#***
#*****
#*******
#*********





n=int(input(""))

#cadena="*"

#for i in range(1,n+1):
#    print(cadena*(2*i-1))

cadena=""
for i in range(n):
    if i ==0:
        cadena=cadena+"*"
    else:
        cadena=cadena+"**"
    print(cadena)












