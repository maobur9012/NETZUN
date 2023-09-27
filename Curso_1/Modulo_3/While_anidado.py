#Crear un prorama que permita ingresar los nombres de N alumnos y la cantidad N de cursos
n = int(input("Ingresa cantidad de estudiantes: "))
i = 1

while n >= i: # 10 != 10 Falso
    nombre = input("ALUMNO {}: ".format(i))
    m = int(input("Ingresa cantidad de cursos: "))
    j = 0
    while m > j:
        curso_nombre = input("CURSO {}: ".format(j+1))
        j += 1
    
    i += 1
    
    