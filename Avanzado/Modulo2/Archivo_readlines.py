#Apertura del archivo
fichero = open(
    "D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/Texto.txt")

#lectura de lionea
lineas = fichero.readlines()
print(type(lineas))
print(lineas)

#Cierre de archivo
fichero.close()
