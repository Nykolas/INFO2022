#Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. 
#El programa debe estar preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee.

c=1
total= 0

while c != 0:

	precio_producto = int(input(f"indique el precio del producto:  "))
	cantidad= int(input("ingrese la cantidad del producto: "))

	total= total + (precio_producto * cantidad)

	c = int(input(" desea seguir: \n 1- si \n 0- no\n opcion:"))

print("el total de la compra es: ", total)
