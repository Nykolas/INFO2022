

#DOS IGUALES SE USA PARA COMPARAR

ingreso = input("INGRESE UNA x: ")
#TAbLAS DE VERDAD
# AND
# V and V ---> V
# V and F ---> F
# F and V ---> F
# F and F ---> F

# or
# V or V ---> V
# V or F ---> V
# F or V ---> V
# F or F ---> F

#CONDICIONAL SIMPLE
if (condicion):
	acciones

# CONDICIONAL ALTERNATIVO
if (ingreso == 'x' or ingreso == 'X'):
	#SE EJECUTA SI LA COND ES VERDADERA
	print("GRACIAS POR INGRESAR LA X")
else:
	#SE EJECUTA SI LA COND ES FALSA
	print("NO INGRESASTE UNA X")

#CONDCIONAL MULTIPLE
#PUEDO PONER LA CANTIDAD DE ELIF QUE NECESITE
#Y PUEDO O NO PONER UN ELSE (DEPENDE SI LO NECESITO)
if (condicion):
	acciones
elif (condicion):
	acciones
elif (condicion):
	acciones
elif (condicion):
	acciones
else:
	acciones