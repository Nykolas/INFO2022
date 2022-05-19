'''

El usuario compra tres productos - Ingresa la cantidad de cada producto que compro - 
calcular el monto total del usuario + iva Les mando de vuelta.

'''
print("WELCOME A MI PROGRAMA ")
print("------------------------------------")

#PIDIO PRECIO Y CANTIDAD DEL PRODUCTO 1
precio_1 = float(input("INGRESE EL PRECIO DEL PRIMER PRODUCTO: "))
cantidad_1 = int(input("INGRESE LA CANTIDAD DE ESE PRODUCTO QUE COMPRO: "))

#PIDIO PRECIO Y CANTIDAD DEL PRODUCTO 2
precio_2 = float(input("INGRESE EL PRECIO DEL SEGUNDO PRODUCTO: "))
cantidad_2 = int(input("INGRESE LA CANTIDAD DE ESE PRODUCTO QUE COMPRO: "))

#PIDIO PRECIO Y CANTIDAD DEL PRODUCTO 3
precio_3 = float(input("INGRESE EL PRECIO DEL TERCER PRODUCTO: "))
cantidad_3 = int(input("INGRESE LA CANTIDAD DE ESE PRODUCTO QUE COMPRO: "))

#CALCULO EL MONTO A PAGAR
monto_total = (precio_1*cantidad_1) + (precio_2*cantidad_2) + (precio_3*cantidad_3)

#LE AGREGO A ESE MONTO EL IVA (21%)
monto_total = monto_total * 1.21

#MUESTRO EL RESULTADO
print("-------------------------------------")
print(f"USTED DEBE PAGAR UN TOTAL DE: ${monto_total}")