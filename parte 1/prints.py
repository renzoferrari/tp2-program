def mostrar_matriz(matriz):
    print("=== NOTAS CARGADAS ===")
    for i in range(len(matriz)):
        print("Alumno " + str(i+1) + ": T1=" + str(matriz[i][0]) + " T2=" + str(matriz[i][1]) + " T3=" + str(matriz[i][2]))

def mostrar_desaprobados(matriz, desaprobados):
    if len(desaprobados) == 0:
        print("No hay alumnos desaprobados")
    else:
        print("=== ALUMNOS DESAPROBADOS ===")
        for i in range(len(desaprobados)):
            indice = desaprobados[i]
            print("Alumno " + str(indice+1))

def mostrar_aplazados(matriz, aplazados):
    if len(aplazados) == 0:
        print("No hay alumnos aplazados")
    else:
        print("=== ALUMNOS APLAZADOS ===")
        for i in range(len(aplazados)):
            indice = aplazados[i]
            print("Alumno " + str(indice+1))

def mostrar_porcentajes(porcentaje_aprobados, porcentaje_desaprobados):
    print("=== PORCENTAJE DE APROBADOS Y DESAPROBADOS ===")
    print("Aprobados: " + str(porcentaje_aprobados) + "%")
    print("Desaprobados: " + str(porcentaje_desaprobados) + "%")

def mostrar_mejor_trimestre(trimestres_ganadores, mayor):
    print("=== TRIMESTRE CON MEJOR PROMEDIO ===")
    print("Promedio: " + str(mayor))
    for i in range(len(trimestres_ganadores)):
        print("Trimestre " + str(trimestres_ganadores[i]))