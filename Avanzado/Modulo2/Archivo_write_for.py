#Apertura de archivo
fichero = open(
    "D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/archivo_write_for.txt", "w")

#Tenemos unos datos que queremos guardar
lista = ["Manzana", "Pera", "Platano"]

#Guardamos la lista en el fichero
for linea in lista:
    fichero.write(linea + "\n")

#Cierre de archivo
fichero.close()