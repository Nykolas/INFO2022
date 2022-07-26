
#ALUMNO: DNI, NOMBRE, SEXO, LEGAJO, CARRERA.


#PROFESOR: DNI, NOMBRE, SEXO, LEGAJO, ANTIGUEDAD.

class Persona:
	def __init__(self, dni,nombre,sexo,legajo):
		self.dni = dni
		self.nombre = nombre
		self.sexo = sexo
		self.legajo = legajo

	def getNombre(self):
		return self.nombre

	def getDni(self):
		return self.dni

	def setNombre(self, nuevo_nombre):
		self.nombre = nuevo_nombre

	def setDni(self, nuevo_dni):
		self.dni = nuevo_dni

	def __str__(self):
		return f"DNI:{self.dni} --- NOMNBRE:{self.nombre}"


class Alumno(Persona):
	def __init__(self,dni,nombre,sexo,legajo,carrera):
		super().__init__(dni,nombre,sexo,legajo)
		self.carrera = carrera

	def getCarrera(self):
		return self.carrera

	def __str__(self):
		return super().__str__() + f"\nCARRERA:{self.carrera}\n SOY UN ALUMNO"

class Profesor(Persona):
	def __init__(self,dni,nombre,sexo,legajo,antiguedad):
		super().__init__(dni,nombre,sexo,legajo)
		self.antiguedad = antiguedad

	def getAntiguedad(self):
		return self.antiguedad

	def getNombre(self):
		x = super().getNombre()
		return f"{self.nombre} SOY PROFE " + x 

	def __str__(self):
		return super().__str__() + f"\nANTIGUEDAD:{self.antiguedad}\n SOY UN PROFESOR"


a = Alumno(30333444,'Nicolas','M',17888,'ISI')
p = Profesor(32555998,'Maria','F',18999,10)

'''
print(a.getNombre())
print("")
print(p.getNombre())
'''
print(a.__dir__())