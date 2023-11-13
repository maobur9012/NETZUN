#Modo 1
diccionario = dict()
print(diccionario)

#Modo 2
d1 = {
    "Nombre": "Edgar",
    "Edad": 32,
    "Documento": 1058969281
}
print(d1)

#Modo 3
d2 = dict([
    ('Nombre', 'Edgar'),
    ('Edad', 32),
    ('Documento', 1058969281),
])
print(d2)

#Modo 4
d3 = dict(Nombre = 'Edgar',
          Edad=32,
          Documento=1058969281)
print(d3)