'''
Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:

i. Si trabaja 40 horas o menos se le paga $16 por hora

ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.
'''

horas = int(input("Ingrese horas trabajadas\t"))

if horas <= 40:
	total = horas * 16
else:
	total = (horas-40)*20 + (40*16)

print(f"Su salario para esta semana es de ${total}")

