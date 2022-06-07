def menu():
	print("-------MENU-------")
	print("1-SUMAR")
	print("2-RESTAR")
	print("3-MULTIPLICAR")
	print("4-DIVIDIR")
	op = input("QUE DESEA?\t")
	return op

def sumar(a,b):
	return a+b

def restar(a,b):
	return a-b

def multiplicar(a,b):
	return a*b

def dividir(a,b):
	if b != 0:
		return a/b
	else:
		return 'ERROR DIVISION POR CERO'

#-----PROGRAMA---------

seguir = 'SI'
print("--------------WELCOME A LA CALCULADORA----------------")

while (seguir.upper() == 'SI'):

	v1 = float(input("INGRESE VALOR 1 \t"))
	v2 = float(input("INGRESE VALOR 2 \t"))

	respuesta = menu()

	if respuesta == '1':
		r = sumar(v1,v2)
	elif respuesta == '2':
		r = restar(v1,v2)
	elif respuesta == '3':
		r = multiplicar(v1,v2)
	elif respuesta == '4':
		r = dividir(v1,v2)

	print(f"EL RESULTADO DE LA OPERACION ES: {r}")

	seguir = input("DESEA REALIZAR OTRA OPERACION? SI O NO.\t")

