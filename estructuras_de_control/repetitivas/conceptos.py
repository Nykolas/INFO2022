
#WHILE
'''
nro = 1
while (nro <= 10):
	print(nro)

print(f"FINAL {nro}")
'''
'''
termino = 'NO'

while (termino.upper() == "NO" ):
	nombre = input("INGRESE NOMBRE DEL ALUMNO/A\t")
	print(f"EL NOMBRE ES---> {nombre}")

	termino = input("YA TERMINO LA CARGA? SI o NO\t")


nombre = "O"
print("SI QUIERE TERMINAR, INGRESE UNA X EN EL NOMBRE")

while (nombre.upper() != "X" ):
	nombre = input("INGRESE NOMBRE DEL ALUMNO/A\t")

	if nombre.upper() != 'X':
		print(f"EL NOMBRE ES---> {nombre}")



termino = True
print("SI QUIERE TERMINAR, INGRESE UNA X EN EL NOMBRE")

while (termino):
	nombre = input("INGRESE NOMBRE DEL ALUMNO/A\t")
	print(f"EL NOMBRE ES---> {nombre}")
	
	salir = input("YA TERMINO LA CARGA? SI o NO\t")

	if salir.upper() == 'SI':
		termino = False 

'''

# FOR

#CONTINUARA.....................