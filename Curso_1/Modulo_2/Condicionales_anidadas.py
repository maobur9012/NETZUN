"""
Selectivas anidadas

Ejemplo:

Crear un programa en python que permita ingresar la edad de una persona e indica si es mayor o menor de edad. si es menor de edad, validad si el valor de la edad es mayor a cero, sino indicar que la edad no es correcta. 

"""


edad = int(input("Ingresar edad: "))

if edad >= 18 :
    print("Mayor de edad")
else:
    if edad > 0:
        print("Menor de edad")
    else: 
        print("Edad no correcta")
    