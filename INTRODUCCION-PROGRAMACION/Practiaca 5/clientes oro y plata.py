#Ejercicio 24 F
#Auxilio Mecánico
#En una empresa de auxilio mecánico existen dos coberturas para los clientes, Oro y Plata. Los
#clientes con cobertura Oro tienen más benecios que los de cobertura Plata y pagan mensualmente un abono mayor. Por ejemplo los clientes Oro tienen usos ilimitados y los clientes Plata
#sólo hasta 5. El sistema ya está funcionando y tenemos que implementar una función particular
#que devuelva el costo para un cliente de un servicio particular.
#Se cuenta con las siguientes funciones y sus valores de retorno:

#cobertura(cliente): retorna un string con los valores "Oro" o "Plata", correspondiente al tipo de cobertura del cliente.
#usados(cliente): retorna un entero que representa la cantidad de servicios que
#ya utilizó el cliente.
#radioDeCobertura(cliente, localidad): devuelve True si el cliente se encuentra
#dentro del radio de cobertura cubierto por la empresa.

#Al recibir un llamado el operador telefónico solicita el número de cliente, la localidad para la
#que solicita la asistencia y le informa el costo del servicio teniendo en cuenta que el servicio no
#tendrá costo para los clientes Oro que estén dentro del área de cobertura y para los clientes Plata
#que les quedaran servicios para usar y estuvieran dentro dicha área. Pagarán $50, los clientes
#Plata dentro del área de cobertura pero ya sin servicios gratis. Pagarán $30 extra los clientes que
#estén fuera del área de cobertura. Observación, los dos últimos montos pueden ser acumulativos.
#Hacer una función llamada pagara que dado un cliente y una localidad devuelva el costo del
#servicio para el cliente.


def pagara(cliente,localidad):
    if (cobertura(cliente)) =="Oro":
         if (radioDeCobertura(cliente,localida)):
            pagra=0
         else:
            pagara=30
    else:
        if radioDeCobertura(cliente,localidad):
            if (usados(cliente))<=5:
                pagara=0
            else:
                pagara=50
        else:
            if (usados(cliente))<=5:
                pagara=50
            else:
                pagara=80
    return pagar











