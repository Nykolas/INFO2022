#CLASES#
class Vehiculo:
	def __init__(self,color,ruedas):
		self.color = color
		self.ruedas = ruedas

	def mostrarsColor(self):
		print(f'Mi color es: {self.color}')

	def mostrarsRuedas(self):
		print(f'Tengo {self.ruedas} ruedas')


class Coche(Vehiculo):
	def __init__(self,velo,cc,color,ruedas):
		super().__init__(color,ruedas)
		self.velocidad = velo
		self.cilindrada = cc

	def mostrarsVelocidad(self):
		print(f'Mi velocidad es: {self.velocidad} KM/H')

	def mostrarsCilindrada(self):
		print(f'Tengo {self.cilindrada} cilindradas')


#PROGRAMA#
color = input("Ingrese el color del Coche:\t")
ruedas = int(input("Ingrese cantidad de ruedas:\t"))
cilindrada = int(input("Ingrese la cilindrada:\t"))
velocidad = int(input("Ingrese la velocidad maxima:\t"))
print("-------------------------------------------------")
#Creamos el objeto 
Auto = Coche(velocidad,cilindrada,color,ruedas)

#LLAMAMOS A LOS METODOS#
Auto.mostrarsCilindrada()
Auto.mostrarsVelocidad()
Auto.mostrarsRuedas()
Auto.mostrarsColor()
