#Realizar un programa que solicite dos numeros y realize la divicion entre ellos,
#no se debe permitit que el denominador sea cero.

n1=float(input("numero"))
n2=float(input("denominador"))

while (n2==0):#no se debe permitir que n2 sea 0.
       n2=float(input(" error ingrese otro denominador: "))

cociente=n1/n2
print("resultado ", cociente)
