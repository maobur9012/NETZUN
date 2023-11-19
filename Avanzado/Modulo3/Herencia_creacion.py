# Definir una clase padre
class Animal:
    pass

#Creamos una clase hija que hereda de la padre

class Perro(Animal):
    pass

print(Perro.__bases__)
#(<class '__main__.Animal'>,)

print(Animal.__subclasses__())
#[<class '__main__.Perro'>]

#La herencia nos permite que la clase hija pueda heredar los metodos y atributos de la clase padre