'''
mi_lista = []

for i in range(5):
	n = int(input("ingrese un numero:\t"))
	mi_lista.append(n)

mi_lista.sort()

print(mi_lista)
print(mi_lista[2])
for x in mi_lista:
	print(f"ELEMENTO {x}")


x = [2,3,7,8,1,5]
y = [2,'nico',50]

z = [2,[1,3,4],[8,7]]

for i in x[1:4]:
	print(i)

'''
#GUARDAR LANOTA DE PW DE CADA UNO

notas = [[5,6,7],[10,9,8],[3,5,6]]

for i in notas:
	#i vale la primera vez [5,6,7]
	#i vale la segunda vez [10,9,8]
	prom = sum(i)/len(i)
	print(f"el promedio de este alumno es--->{round(prom,2)}")

