d1 = {
    "Nombre":"Edgar",
    "Edad": 32,
    "Documento": 1058969281
}

# 1. Imprime los key del diccionario
for x in d1:
    print(x)
#Nombre
#Edad
# Documento

# 2. Imprime los valores del dicionario
for x in d1:
    print(d1[x])
#Edgar
#32
#1058969281

# 3. Imprime los key y value del diccionario
for x, y in d1.items():
    print(x, y)
#Nombre Edgar
#Edad 25
#Documento 1058969281

    