#Apertura del archivo
fichero = open(
    "D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/Texto.txt", "r")

#Lectura de linea
lineas = fichero.readlines()

for oracion in lineas:
    print(oracion, end="")

#Cierre de archivos.
fichero.close()