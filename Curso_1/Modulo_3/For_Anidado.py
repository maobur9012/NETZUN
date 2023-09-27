"""
Crear un programa que permita ingresar los nombres de N alumnos y cantidad M de cursos por alumno
"""
n = int(input("Ingrese cantidad de alumnos: "))
for i in range(n):
    nombre = input("ALUMNO {}: ".format(i))
    m = int(input("Ingresar cantidad de cursos: "))
    for j in range(m):
        curso_nombre = input("CURSO {}: ".format(j+1))


