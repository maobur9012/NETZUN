class Animal:
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad
        
    #Metodo generico pero con implementacion particular
    def hablar(self):
        #Metodo vacio
        pass
    
    #Metodo generico pero con implementacion particular
    def moverse(self):
        #Metodo vacio
        pass
    
    #Metodo generico con la misma implementacion
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

class Mamifero(Animal): # La clase mamifero es hijo de la clase animal
    def __init__(self, especie, edad) -> None:
        super().__init__(especie, edad)

class Perro(Mamifero): # la clase perro es hijo de la clase mamifero pero por herencia multiple, perro hereda lo que tenga la clase animal
    def __init__(self, especie, edad, dueno) -> None:
        super().__init__(especie, edad)
        self.dueno = dueno

mi_perro = Perro("Toby", "Bulldog", "Edgar")
mi_perro.describeme()
    

    
