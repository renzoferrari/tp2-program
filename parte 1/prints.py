def mostrar_matriz(matriz: list) -> None:
    """
    Muestra la matriz con las notas de cada alumno.
    """
    print("=== NOTAS CARGADAS ===")
    for i in range(len(matriz)):
        print("Alumno " + str(i+1) + ": T1=" + str(matriz[i][0]) + " T2=" + str(matriz[i][1]) + " T3=" + str(matriz[i][2]))

def mostrar_alumnos(lista: list, mensaje_vacio: str, titulo: str) -> None:
    """
    Muestra los alumnos de la lista recibida.
    Recibe el mensaje en caso de lista vacia y el titulo como parametro.
    """
    if len(lista) == 0:
        print(mensaje_vacio)
    else:
        print(titulo)
        for i in range(len(lista)):
            print("Alumno " + str(lista[i] + 1))

def mostrar_porcentajes(porcentaje_aprobados: float, porcentaje_desaprobados: float) -> None:
    """
    Muestra el porcentaje de aprobados y desaprobados.
    """
    print("=== PORCENTAJE DE APROBADOS Y DESAPROBADOS ===")
    print("Aprobados: " + str(porcentaje_aprobados) + "%")
    print("Desaprobados: " + str(porcentaje_desaprobados) + "%")

def mostrar_mejor_trimestre(trimestres_ganadores: list, mayor: float) -> None:
    """
    Muestra el trimestre con mejor promedio.
    """
    print("=== TRIMESTRE CON MEJOR PROMEDIO ===")
    print("Promedio: " + str(mayor))
    for i in range(len(trimestres_ganadores)):
        print("Trimestre " + str(trimestres_ganadores[i]))