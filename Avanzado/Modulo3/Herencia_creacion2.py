class Animal:
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad
    
    #Metodo generico pero con implementacion particular
    def hablar(self):
        # Metodo vacio
        pass
    
    #Metodo generico pero con implementacion particular    
    def moverse(self):
        # Metodo vacio
        pass
    
    #Metodo generico con la misma implementacion
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

class Perro(Animal):
    def hablar(self):
        print("Guau")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):    
    def hablar(self):
        print("Muuuu")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):    
    def hablar(self):
        print("Bazzz!")
    def moverse(self):
        print("Volando")
    #Nuevo metodo
    def picar(self):
        print("Picar!")

mi_perro = Perro('mamifero', 10)
mi_vaca = Vaca('mamifero', 23)
mi_abeja = Abeja('insecto', 1)

mi_perro.hablar()
mi_vaca.hablar()

mi_vaca.describeme()
mi_abeja.describeme()

mi_abeja.picar()

print(mi_perro.edad)
print(mi_perro.especie)