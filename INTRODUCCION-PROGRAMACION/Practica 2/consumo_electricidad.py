#Ejercicio 10 F
#Hacer en pseudocodigo y luego un programa que calcule el importe que se le facturarÃƒÆ’Ã‚Â¡ a un
#cliente por consumo de electricidad sabiendo que la compaÃƒÆ’Ã‚Â±ÃƒÆ’Ã‚Â­a que se la provee cobra una tarifa
#fija de 480 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra
#a 25,5 pesos el KW, ademÃƒÆ’Ã‚Â¡s se agregan $78 de impuestos. Se leen los valores del medidor al
#comienzo y al final del perÃƒÆ’Ã‚Â­odo.

#DATO:
#TARIFA FIJA:LO QUE SIEMPRE SE COMPRA AL USUARIO.
#IMPUESTOS:SIEMPRE SE LE COBRA AL USUARIO: $78.
#COSTO POR KW EXCEDENTE: $25.5.
print ("Este programa calcula el precio a pagar en la factura de LUZ")

TARIFA_FIJA=480
IMPUESTOS=78
LIMITE_KWS_INCLUIDOS=200
PRECIO_EXCEDENTE=25.5

kwinicial=float(input("Ingrese KW iniciales"))
kwfinal=float(input("Ingrese KW final"))
kw=kwfinal-kwinicial
montofinal=TARIFA_FIJA + IMPUESTOS
if(kw>LIMITE_KWS_INCLUIDOS):
   montofinal=montofinal+(kw-LIMITE_KWS_INCLUIDOS)*PRECIO_EXCEDENTE
print("El precio a pagar es:",montofinal)
