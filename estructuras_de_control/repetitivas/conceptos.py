
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
'''
N = 10
N = int(input("INGRESE LA CANTIDAD"))

for (i = 1 hasta N; i + 1) {
	# i siempre siempre es un entero
}
'''

#iterable : Cualquier estructura de datos que sea iterable.

# nicolas
#(1,2,3,4,5,6) tupla 
#[1,2,3,4,5] lista
#{clave:valor} diccionario
#objetos

# Rango --> (vi,vf,incremnto) ---> (1,10,1)--> (1,2,3,4,5,6,7,8,9)
#POR DEFECTO EL vi = 0, y el incremento = 1
# (5) --> (0,1,2,3,4)


print("FOR-------")
n = int(input("ingrese cuantos numeros quiere mostrar "))

for i in range(n):
	print(i)

