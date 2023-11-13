import pandas as pd

# lee el archivo CSV

df = pd.read_csv("D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/paises.csv")

# Filtrado
filter = df['iso'] == "AE"
df_enuso = df.where(filter).notna()
print(df_enuso)