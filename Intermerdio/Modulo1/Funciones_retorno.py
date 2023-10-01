#Valores de retorno, devuelve el resultado

def suma(a, b):
    suma = a + b 
    return suma

def resta(a, b):
    resta = a - b
    return resta

def multiplicacion(x1, x2):
    resultado = x1 * x2
    return resultado

def funcion_parametros(a):
    print(a)

funcion_parametros("Soy una funcion con 1 parametro")    

sumartoria = suma(15, 5)
print(sumartoria)

resta_resultado = resta(10, 2)
print(resta_resultado)

multi = multiplicacion(10, 5)
print(multi)