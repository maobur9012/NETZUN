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
    def __init__(self, especie, edad, dueno) -> None:
        #Alternativa
        
        #self.especie = especie
        #self.edad = edad
        #self.dueño = dueño
        
        #Alternativa 2
        super().__init__(especie, edad)
        self.dueno = dueno
mi_perro = Perro("X", 5, "Edgar")
print(mi_perro.dueno)