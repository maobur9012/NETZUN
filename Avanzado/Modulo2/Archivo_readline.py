#Apertura de archivo

fichero = open(
    "D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/Texto.txt")

#Lectura de linea
linea = fichero.readline()
print(type(linea))
print(linea)
print(fichero.readline())


#cierre de archivo
fichero.close()