import pandas as pd

# lee archivo CSV
# dataframe - tipo de dato propio de pandas

df = pd.read_csv("D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/paises_ejemplo.csv")

# muestra las primeras filas
print(df.head())#Muestra los primeros 5 primeros datos de la tabla
print(df)