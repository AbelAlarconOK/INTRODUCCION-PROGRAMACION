#Ejercicio 16 F
#Determinar cuántos segundos tiene una hora, y cuántos tiene un día.
#Escribir una expresión matemática que transforme un lapso de tiempo expresado
#en segundos a unoexpresado en minutos.
#Escribir otra para transformar a horas y una última que transforme a días.
#Escribir un programa en Python que pida al usuario una cantidad de segundos
#y muestre cuantos minutos son, así como también cuantas horas y cuantos días.

cantSegundos = int(input("cantidad de segundos:"))

#Transformo a minutos.

cantminutos = cantSegundos//60

#Transformo a horas.

canthoras = cantSegundos//3600

#transformo a dia-

cantdias = cantSegundos//86400

print("los segundos ingresados son: ", cantSegundos)
print("la cantidad de minutos es : ", cantminutos)
print("la cantidad de horas son: ",  canthoras)
print("la cantidad de dias son: ", cantdias)



segundosIngresados=int(input("ingresar segundos"))
minutos=60 #segundos
horas=minutos*60 #3600 segundos
dias=horas * 24 #86400 segundos

print(segundosIngresados//dias, "dia(s)",
(segundosIngresados%dias)//horas, "hora(s)",
((segundosIngresados%dias)%horas)//minutos, "minuto(s)",
(((segundosIngresados%dias)%horas)%minutos), "segundo(s)"
)


print ("Este programa calcula los segundos en dias horas minutos y segundos BIEN")
s_tot=int(input("Ingrese la cantidad de segundos: "))

m_tot = s_tot // 60	# total minutos
h_tot = m_tot // 60	# total horas
d_tot = h_tot // 24	# total dias

s_res = s_tot - m_tot * 60	# resto segundos
m_res = m_tot - h_tot * 60	# resto minutos
h_res = h_tot - d_tot * 24	# resto horas

print ("La cantidad de dias es: ",d_tot)
print ("La cantidad de horas es: ",h_res)
print ("La cantidad de minutos es: ",m_res)
print ("La cantidad de segundos es: ",s_res)


