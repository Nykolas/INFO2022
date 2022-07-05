

class Producto:

	#SE EJECUTA SIEMPRE AL CREAR UN OBJETO
	def __init__(self,nom,prec,sto,marca = '0'):
		self.nombre = nom
		self.precio = prec
		self.stock = sto
		self.precio_por_mayor = self.precio * 0.8
		self.marca = marca

	def mostrar_nombre(self):
		print(f"Mi nombre es {self.nombre}")

	def mi_stock(self):
		print(f"Mi stock es {self.stock}")

	def cambiar_stock(self,nuevo):
		self.stock = nuevo

	def mostrar_precios(self):
		print(f"mi precio por menor es-->{self.precio}\nmi precio por mayo res -->{self.precio_por_mayor}")

	def cambiar_marca(self,nueva):
		self.marca = nueva

	def mostrar_marca(self):
		print(f"mi marca es {self.marca}")


#AFUERA

p1 = Producto('yerba',100,50)

p2 = Producto('leche',150,10)


p1.mostrar_marca()

#ENCAPSULADO
p1.cambiar_marca('Rosamonte')
#SIn ENCAPSULAR
p1.marca = 'Playadito'

p1.mostrar_marca()
