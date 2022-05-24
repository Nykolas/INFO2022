# Determinar el número mayor de 10 números ingresados.

mayor = 0

for nro in range(1,11):

	valor = int(input(f"ingrese el numero {nro}:\t"))
	
	if valor > mayor:
		mayor = valor


print(f"EL numero mayor de todos los ingresados es: {mayor}")
