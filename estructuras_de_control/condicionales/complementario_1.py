# Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.

n1 = int(input("Ingrese el primer numero\t"))
n2 = int(input("Ingrese el segundo numero\t"))
n3 = int(input("Ingrese el tercer numero\t"))


#N1 MAS GRANDE
if n1 > n2 and n1 > n3:
	#CUAL ES EL SEGUNDO DESPUES DE N1
	if n2 > n3:
		print(f"los números de mayor a menor son: {n1} \t {n2}\t {n3}")
	else:
		print(f"los números de mayor a menor son: {n1} \t {n3}\t {n2}")

#N2 MAS GRANDE	
elif n2> n1 and n2 > n3:
	if n1 > n3:
		print(f"los números de mayor a menor son: {n2} \t {n1}\t {n3}")
	else:
		print(f"los números de mayor a menor son: {n2} \t {n3}\t {n1}")

#N3 MAS GRANDE			
elif n3 > n1 and n3 > n2:
	if n1 > n2:
		print(f"los números de mayor a menor son: {n3} \t {n1}\t {n2}")
	else:
		print(f"los números de mayor a menor son: {n3} \t {n2}\t {n1}")

else:
	if n1 == n3:
		print(f"los números de mayor a menor son: {n3} \t {n1}\t {n2}")
	elif n2 == n3:
		print(f"los números de mayor a menor son: {n3} \t {n2}\t {n1}")
	else:
		print(f"los números de mayor a menor son: {n1} \t {n2}\t {n3}")
