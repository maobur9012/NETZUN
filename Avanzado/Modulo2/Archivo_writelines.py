#Apertura de archivo
fichero = open(
    "D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/archivo_writelines.txt", "w")

#Tenemos unos datos que queremos guardar
lista = ["Manzana", "Pera", "Platano"]

fichero.writelines(lista)
fichero.close

#Se guarda
# ManzanaPeraPlatano
