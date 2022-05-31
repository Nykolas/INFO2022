

fila = int(input("ingrese fil:\t"))
columna = int(input("ingrese col:\t"))

if columna%2 == 0:
	impar = False
else:
	impar = True

for f in range(fila):
	for i in range(columna//2):
		if f%2 == 0:
			print("[V]", end ="")
			print("[A]", end ="")
		else:
			print("[A]", end ="")
			print("[V]", end ="")


	#AFUERA DEL FOR i		
	if impar:
		
		if f%2 == 0:
			print("[V]", end ="")
		else:
			print("[A]", end ="")

	print("")

