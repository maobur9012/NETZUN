print("Ejemplo con REMOVE")

lista_letras = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l']
print(lista_letras)

if 'c' in lista_letras:
    lista_letras.remove('c')
else:
    print("No esta dentro de la lista")

print(lista_letras)