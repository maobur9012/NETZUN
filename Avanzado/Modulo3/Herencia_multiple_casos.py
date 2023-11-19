class Clase1: #Clase1 padre
    pass

class Clase2(Clase1): #Clase2 hijo de clase1
    pass

class Clase3(Clase2): #Clase3 es hijo de clase2 -> tambien es hijo de Clase1
    pass

print(Clase3.__mro__)