lista_letras = ['a', 'b', 'c', 'd', 'e', 1, 2, 19.0]
variable = 'c'

if variable in lista_letras: #Verifico que se encuntre dentro de la lista
    posicion = lista_letras.index(variable) # pido el indice
    print("Esta es la posicion: ", posicion)
else:
    print("No hay elemento en la lista")
