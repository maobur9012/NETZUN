def numeros_mayor(numero_1, numero_2):
    respuesta = False
    if numero_1 > numero_2:
        respuesta = True
    
    return respuesta

x = int(input("Numero 1: "))
y = int(input("Numero 2: "))

if numeros_mayor(x, y):
    print("El numero {} es mayor a {}".format(x, y))
else :
    print("El numero {} es menor a {}".format(x, y))



