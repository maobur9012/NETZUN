matriz = []

FILAS = 4
COLUMNAS = 6

#Lllenar matriz
for i in range(FILAS): #4 veces
    fila = [1] * COLUMNAS #[0,0,0,0,0,0]
    matriz.append(fila)
    
#Imprimiendo matriz
print("Recorrido de matriz por medio de FOR")

for i in range(FILAS): # repite 4 veces
    for j in range(COLUMNAS): # repite 6 veces
        print(matriz[i][j], end=" ")
    print()