"""
* Crear un programa en python que permita ingresar un numero e indicar si es positivo, negativo  o cero
"""
num = int(input("Ingrese un numero: "))

if num > 0 :
    print("Ingresaste un numero positivo.")
elif num < 0 :
    print("Ingresaste un numero negativo.")
else :
    print("Ingresaste cero")