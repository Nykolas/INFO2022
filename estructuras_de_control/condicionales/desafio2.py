'''
Para seguir colaborando en esta misión de salvar al planeta, 
necesitamos que elabores un programa en Python que dado el tamaño de un pez 
indique si su organismo está contaminado. Para ello tendremos 4 opciones:

Tamaño Normal: Mensaje "Pez en buenas condiciones"
Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
Tamaño sobredimensionado: Mensaje "Pez contaminado"
'''

print("EL TAMAÑO DEL PEZ ES: ")
print("1- NORMAL")
print("2- DEBAJO DE LO NORMAL")
print("3- ENCIMA DE LO NORMAL")
print("4- SOBREDIMENSIONADO")

tamaño = input()

if tamaño == "1":
	print("Pez en buenas condiciones")
elif tamaño == "2":
	print("Pez con problemas de nutrición")
elif tamaño == "3":
	print("Pez con síntomas de organismo contaminado")
else:
	print("Pez contaminado")