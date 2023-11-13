matriz = []
ALUMNOS = 4
NOTAS = 3

#LLenar matriz
for i in range(ALUMNOS): # 4 veces
    notas = []
    print("ALUMNO: {}".format(i + 1))
    for j in range(NOTAS):
        nota = float(input("Nota {}: ".format(j + 1)))
        notas.append(nota)
    matriz.append(notas)

#Recorrer matriz
print("Recorrido de matriz por medio de FOR")

for i in range(ALUMNOS): # repite 4 veces
    for j in range(NOTAS): # repite 6 veces
        print(matriz[i][j], end=" ")
    print()