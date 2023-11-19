class Perro:
    #El metodo __init__  es lllamado al crear el objeto
     
     # Metodo constructor
     def __init__(self, nombre, raza, edad):
          print(f"Creando perro {nombre}, {raza}, {edad}")
          
          #Atributos de la instancia
          self.nombre = nombre
          self.raza = raza
          self.edad = edad

mi_perro = Perro("Toby", "Bulldog", 4)
print(type(mi_perro))
#Creando perro Toby, Bulldog
#<class '__main__.Perro'>

print(mi_perro.nombre) #Toby
print(mi_perro.raza)  #Bulldog
print(mi_perro.edad)  #4

class Alumno:
    def __init__(self, nombre, apellido, edad) -> None:
         
         self.nombre = nombre
         self.apellido = apellido
         self.edad = edad
alumno_1 = Alumno("Edgar", "Burbano", 32)
print(alumno_1.nombre)
print(alumno_1.apellido)
print(alumno_1.edad)