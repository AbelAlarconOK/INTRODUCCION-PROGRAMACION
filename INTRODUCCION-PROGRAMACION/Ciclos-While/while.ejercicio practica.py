#HACER UN PROGRAMA QUE VALIDE EL INGRESO AL SISTEMA USANDO UNA CONTRASEÑA.
#MIENTRAS LA CONTRASEÑA SEA INVALIDA, LE VOLVERA A PEDIR AL USUARIO QUE
#INGRESE NUEVAMENTE LA MISMA INFINITA VECES.

contraseña="riverplate"
n_contraseña=input("ingrese la contraseña")
while (contraseña!=n_contraseña):
    print("volver a ingresar contraseña")
    n_contraseña=input("ingrese la contraseña nuevamente")
print("bienvenido")
