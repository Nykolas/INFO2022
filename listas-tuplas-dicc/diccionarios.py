
#[ [nombre,numero] , [nombre,numero]]

# diccionarios: { clave:valor, clave:valor }
#valor: puede ser cualquier cosa.


#{nombre: numero, nombre:numero }

'''
agenda = {}

#agenda[clave] = valor

agenda['nicolas'] = 3624245588
agenda['renzo'] = 3624887968
agenda['lucas'] = 10000000
agenda['noelia'] = 10000000
agenda['carlos'] = [3645133123,364756318]

# NOS RETORNA LAS CLAVES agenda.keys()
# NOS RETORNA LOS VALORES agenda.values()
# NOS RETORNA CADA PAR CLAVE VALOR COMA UNA TUPLA agenda.items()
print(agenda)
print("")

# [(nombre,numero),(nombre,numero)] --> esto es agenda.items()


for x in agenda.items():
	print(f"{x[0]} --> {x[1]}")


for clave,valor in agenda.items():

	print(f"{clave} --> {valor}")


# GUARDAR LA INFO DE TODOS LOS ESTUDIANTES DEL INFO
# DNI, NOMBRE, SEXO, EDAD.

{	
	dni: [nombre,sexo,edad] ,
	dni: [nombre,sexo,edad]
}


{
	dni: {'nombre':nombre, 'sexo': sexo, 'edad':edad},
	dni: {'nombre':nombre, 'sexo': sexo, 'edad':edad},
}
'''

estudiante = {}

for i in range(3):
	dni = input("DNI:\t ")
	nombre = input("NOMBRE\t ")
	sexo = input("SEXO\t")
	edad = input("EDAD\t")

	cada_uno = {}
	cada_uno['nombre'] = nombre
	cada_uno['sexo'] = sexo
	cada_uno['edad'] = edad

	#OTRA FORMA
	#cada_uno = {'nombre':nombre,'sexo':sexo,'edad':edad}

	estudiante[dni] = cada_uno

print(estudiante)
print(" ")

for k,v in estudiante.items():
	print(f"ESTUDIANTE DNI: {k}")
	for x,i in v.items():
		print(f"{x}--->{i}")






