
#DADO EL MONTO DE COMPRA DE UN CLIENTE
#si LA COMPRA es MAYOR A 10000 DESCONTAR 5%
#si la compra es mayor a 15000 descontar 10%
#si la compra es mayor a 50000 descontar un 20%
#si la compra es mayor a 100000 descontar un 30%
# MOSTRAR AL FINAL EL MONTO TOTAL Y EL DESCUENTO REALIZADO


monto = float(input("INGRESE EL MONTO TOTAL DE SU COMPRA: "))

if (monto > 100000):
	descuento = monto * 0.3
	monto = monto - descuento
	print(f"EL MONTO TOTAL A PAGAR ES DE ${monto} Y SE LE DESCONTO 30% que equivale a ${descuento}")
elif (monto > 50000):
	descuento = monto * 0.2
	monto = monto - descuento
	print(f"EL MONTO TOTAL A PAGAR ES DE ${monto} Y SE LE DESCONTO 20% que equivale a ${descuento}")
elif (monto > 15000):
	descuento = monto * 0.1
	monto = monto - descuento
	print(f"EL MONTO TOTAL A PAGAR ES DE ${monto} Y SE LE DESCONTO 10% que equivale a ${descuento}")
elif (monto > 10000):
	descuento = monto * 0.05
	monto = monto - descuento
	print(f"EL MONTO TOTAL A PAGAR ES DE ${monto} Y SE LE DESCONTO 5% que equivale a ${descuento}")
else:
	print(f"EL MONTO TOTAL A PAGAR ES DE ${monto} NO SE APLICARON DESCUENTOS")