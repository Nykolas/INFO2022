
#DADO EL MONTO DE COMPRA DE UN CLIENTE, OFRECER UN DESCUENTO DEL 10%
#SIEMPRE Y CUANDO LA COMPRA SEA MAYOR A #10000
#PERO SI LA MISMA ES MENOR O IGUAL A 10000, iNRREMENTARLE UN 5%


monto = float(input("INGRESE EL MONTO TOTAL DE SU COMPRA: "))


if (monto > 10000):
	descuento = monto * 0.1 #(monto * 10/100)
	monto = monto - descuento
	print(f"EL MONTO TOTAL A PAGAR ES DE ${monto} Y SE LE DESCONTO 10% que equivale a ${descuento}")
else:
	aumento = monto * 0.05 #(monto * 5/100)
	monto = monto + aumento
	print(f"EL MONTO TOTAL A PAGAR ES DE ${monto} Y SE LE INCREMENTO UN 5% que equivale a ${aumento}")
