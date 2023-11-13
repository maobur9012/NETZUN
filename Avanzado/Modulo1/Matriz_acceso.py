pbi = [[2.9, 2.5], [3.9, 4.0], [0.9, 2.2], [1.5, 3.3],
       [1.8, 2.6], [1.0, 2.0], [2.2, 2.3], [4.0, 4.0],
       [2.5, 3.5], [3.0, 3.0], [-9.5, -8.5]]

FILAS = 11
COLUMNAS = 2

for i in range(FILAS): # i en la posicion 0
    for j in range(COLUMNAS): # j en la posicion 0
        print(pbi[i][j], end= "  ") #pbi[2][1]
    print( )
    
item = pbi[2][1] # [i][j] ==> i: fila, j: columna
print(item) 


for i in range(FILAS):
    for j in range(COLUMNAS):
        print(pbi[i][j], end="  ")
    print( )