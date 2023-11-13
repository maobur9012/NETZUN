import pandas as pd

# lee el archivo CSV
df = pd.read_csv("D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/paises.csv")

#Acceso por posicion de filas
#print(df[5:10])

#Acceso por columnas
print(df[["name","nombre","iso"]])
