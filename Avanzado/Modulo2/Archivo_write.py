#Apertura de archivo
fichero = open(
    "D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/archivo_write.txt", "w")

#Escritura al texto
fichero.write("Edgar Mauricio Burbano\n")
fichero.write("Python\n")
fichero.write("Colombia")

#Cierre de archivo
fichero.close()