#Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas.


A=int(input(f"ingrese A\t"))
B=int(input(f"ingrese multiplicador(B)\t"))

resultado = 0

for i in range(B):
	resultado = resultado + A

print(f"el resultado es {resultado }")



# A = 4 y B = 3
# EL FOR SE VA A EJECUTAR 3 veces

#resultado = 0

#1 iteracion resultado = rresultado + A ---> resultado = 0 + 4
# resultado vale 4

#2 iteracion resultado = resultado + A ---> resultado = 4 + 4
# resultado vale 8

#3 iteracion resultado = rresultado + A ---> resultado = 8 + 4
# resultado vale 12

# FINAL RESULTADO = 12
