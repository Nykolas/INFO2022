'''
Un grupo de 100 estudiantes presentan un exámen de Física. 
Diseñe un diagrama que lea por cada estudiante la calificación obtenida y calcule e imprima:

A.- La cantidad de estudiantes que obtuvieron una calificación menor a 50.

B.- La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70.

C.- La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.

D.- La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
'''

ra = 0
rb = 0
rc = 0
rd = 0

for est in range(1,101):
	nota = int(input(f"ingrese la calificacion del estudiante {est}\t"))

	if nota < 50:
		ra += 1  # ra = ra + 1
	elif nota < 70:
		rb += 1
	elif nota < 80:
		rc += 1
	else:
		rd += 1

print("---------------RESULTADOS---------------------")

print(f"la cantidad de estudiantes que sacaron nota menor a 50 es:\t {ra}")
print(f"la cantidad de estudiantes que sacaron nota mayor a 50 y menor a 70 es:\t {rb}")
print(f"la cantidad de estudiantes que sacaron nota mayor a 70 y menor a 80 es:\t {rc}")
print(f"la cantidad de estudiantes que sacaron nota mayor a 80 es:\t {rd}")