
#FUNCION SIN PARAMETROS Y QUE NO RETORNA NADA
def saludar():
	print("HOLA A TODOS/AS.. ")

#FUNCION SIN PARAMETROS Y SI RETORNA
def obtenerNombre():
	nombre = input("INGRESA TU NOMBRE\t")
	apellido = input("INGRESA TU APELLIDO\t")
	completo = nombre + ', ' + apellido
	return completo

#FUNCION CON PARAMETROS
def suma(a,b):
	resul = a+b
	return resul


#------MI PROGRAMA---------
#saludar()
#--------------------------
#NYA = obtenerNombre()
#--------------------------
#x = float(input("INGRESA VALOR 1:\t"))
#y = float(input("INGRESA VALOR 2:\t"))
#r = suma(x,y)
#print(F"el resultado es {r}")
#--------------------------

#PARAMETRO POR DEFECTO
def mostrar(a=50, b=70, c=1000):

	print(f"valor a: {a}")
	print(f"valor b: {b}")
	print(f"valor c: {c}")


mostrar(b=10, a ="nico", c = 8)