def suma():
    a = int(input("Ingresar el numero1: "))
    b = int(input("Ingresar el numero1: "))
    suma = a + b
    #return suma 
    print(suma)

def calculadora(x, y):
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    return suma, resta, multiplicacion

a, b, c = calculadora(10,5)
print(a, b, c)
    