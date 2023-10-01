# Positivos
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("Valor que se encuentra en el indice 1: ", dias[1])
print("Valores que se encuentra en el indice inicial 0 hasta 2: ",dias[:3])
print("Valores que se encuentra en el indice inicial 3 hasta 6: ",dias[3:])
print("Valores desde el indice  3 hasta el indice 4: ",dias[3: 5])

#Negativos

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print("Valor que se encuentra en el ultimo indece 6: ", dias[-1])
print("Valor que se encuentra en el indece 2: ", dias[-5])
print("Valor que se encuentra en el indice 4: ", dias[-3])
print("Valores que se encuentran desde el indice 4 hasta 6 que es el indice final: ", dias[-3:])

#Utilizando LEN
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print("Cantidad de elementos", len(dias))
print(dias[len(dias)-1])

