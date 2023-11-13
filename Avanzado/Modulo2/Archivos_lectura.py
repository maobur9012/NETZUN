#Apertura de archivo

fichero = open(
    "D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/Texto.txt", "r")

# 'r': por defecto para leer el fichero
# 'w': para escribir en el fichero

#Lectura de todo el fichero
print(fichero.read())

#Cierre de archivo
fichero.close()