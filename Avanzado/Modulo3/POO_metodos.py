class Perro:
    #Atributo de clase
    especie = 'mamifero'
     
     # Metodo constructor/ el metodo _init__ es llamado al crear el objeto
    def __init__(self, nombre, raza, edad):
          print(f"Creando perro {nombre}, {raza}, {edad}")
          
          #Atributos de la instancia
          self.nombre = nombre
          self.raza = raza
          self.edad = edad
          
    def ladra(self):
        print("Guau")
    
    def camina(self, pasos):
        print(f"Caminando  {pasos}  pasos")

mi_perro = Perro("Toby", "Bulldog", 4)
mi_perro.ladra()
mi_perro.camina(50)

#print(type(mi_perro))
#Creando perro Toby, Bulldog
#<class '__main__.Perro'>


class Alumno:
    def __init__(self, nombre, apellido, edad) -> None:
         
         self.nombre = nombre
         self.apellido = apellido
         self.edad = edad
    
    def rendir_examen(self):
        print("Tomando examen en aula")
    
    def asitir(self):
        print("Asistiendo puntual")
    
alumno_1 = Alumno("Edgar", "Burbano", 32)
print(alumno_1.nombre)
print(alumno_1.apellido)
print(alumno_1.edad)
alumno_1.asitir()
alumno_1.rendir_examen()


