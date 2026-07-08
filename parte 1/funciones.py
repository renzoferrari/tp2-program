from inputs import *

def cargar_notas_manual(cantidad_alumnos: int) -> list:
    """
    Carga las notas de los alumnos manualmente.
    Recibe la cantidad de alumnos como parametro.
    Retorna la matriz con las notas.
    """
    matriz = []
    for i in range(cantidad_alumnos):
        fila = []
        for j in range(3):
            nota = pedir_nota("Ingrese nota del alumno " + str(i+1) + " trimestre " + str(j+1) + ": ")
            fila.append(nota)
        matriz.append(fila)
    return matriz

def obtener_alumnos_con_nota_menor(matriz: list, limite: int) -> list:
    """
    Retorna una lista con los indices de alumnos que tienen
    al menos una nota menor al limite recibido.
    """
    resultado = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < limite:
                resultado.append(i)
                break
    return resultado

def calcular_porcentaje_aprobados(matriz: list) -> float:
    """
    Retorna el porcentaje de alumnos aprobados.
    """
    aprobados = len(matriz) - len(obtener_alumnos_con_nota_menor(matriz, 7))
    return int(aprobados * 100 / len(matriz) * 100) / 100

def calcular_porcentaje_desaprobados(matriz: list) -> float:
    """
    Retorna el porcentaje de alumnos desaprobados.
    """
    desaprobados = len(obtener_alumnos_con_nota_menor(matriz, 7))
    return int(desaprobados * 100 / len(matriz) * 100) / 100

def calcular_promedios_trimestres(matriz: list) -> list:
    """
    Retorna una lista con el promedio de cada trimestre.
    """
    promedios = []
    for j in range(3):
        suma = 0
        for i in range(len(matriz)):
            suma = suma + matriz[i][j]
        promedio = int(suma / len(matriz) * 100) / 100
        promedios.append(promedio)
    return promedios

def obtener_mayor_promedio(promedios: list) -> float:
    """
    Retorna el mayor promedio de la lista de promedios.
    """
    mayor = promedios[0]
    for i in range(len(promedios)):
        if promedios[i] > mayor:
            mayor = promedios[i]
    return mayor

def obtener_trimestres_ganadores(promedios: list, mayor: float) -> list:
    """
    Retorna una lista con los trimestres que tienen el mayor promedio.
    """
    trimestres_ganadores = []
    for i in range(len(promedios)):
        if promedios[i] == mayor:
            trimestres_ganadores.append(i + 1)
    return trimestres_ganadores