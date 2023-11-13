fichero = open(
    "D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/Texto.txt", "r")
oracion = fichero.readline()
#Lectura con while
while oracion != "":
    print(oracion, end="")
    oracion = fichero.readline()