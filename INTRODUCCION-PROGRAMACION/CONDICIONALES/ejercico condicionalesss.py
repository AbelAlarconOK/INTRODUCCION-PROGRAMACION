#HACER UN PROGRAMA QUE SOLICITE QUE SOLICITE DOS NUMEROS E INDIQUE
#EL SIGNO DE LA MULTIPLICACION SIN EFECTUARLA.


n1=int(input("ingrese primer numero: "))
n2=int(input("ingrese segundo numero: "))
if(n1==0 or n2==0):
    print("es igual : 0" )
else:
  if (n1>0 and n2>0) or ( n1<0 and n2<0):
    print("+")
  else:
    print("-")


#INTRODUCIR DOS NUMEROS ENTEROS POR EL TECLADO DIVIDIENDO Y DIVISOR.
#SI DIVIDIENDO ES DIVISIBLE POR DIVISOR EL PROGRAMA DEBE MOSTRAR: "DIVISIBLES,
#EN CASO CONTRARIO "INDIVISIBLE"

n1=int(input("ingrese primer numero: "))
n2=int(input("ingrese segundo numero: "))

if (n1%n2== 0):
    print("DIVISIBLE")
else:
    print("INDIVISIBLE")

