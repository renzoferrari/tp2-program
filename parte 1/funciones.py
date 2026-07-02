from inputs import *

def cargar_notas_manual():
    matriz = []
    for i in range(7):
        fila = []
        for j in range(3):
            nota = pedir_nota("Ingrese nota del alumno " + str(i+1) + " trimestre " + str(j+1) + ": ")
            fila.append(nota)
        matriz.append(fila)
    return matriz 

def obtener_desaprobados(matriz):
    desaprobados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < 7:
                desaprobados.append(i)
                break
    return desaprobados

def obtener_aplazados(matriz):
    aplazados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < 4:
                aplazados.append(i)
                break
    return aplazados

def calcular_porcentaje_aprobados(matriz):
    desaprobados = obtener_desaprobados(matriz)
    total = len(matriz)
    cantidad_desaprobados = len(desaprobados)
    cantidad_aprobados = total - cantidad_desaprobados
    porcentaje_aprobados = int(cantidad_aprobados * 100 / total * 100) / 100
    porcentaje_desaprobados = int(cantidad_desaprobados * 100 / total * 100) / 100
    return porcentaje_aprobados, porcentaje_desaprobados

def calcular_promedios_trimestres(matriz):
    promedios = []
    for j in range(3):
        suma = 0
        for i in range(len(matriz)):
            suma = suma + matriz[i][j]
        promedio = int(suma / len(matriz) * 100) / 100
        promedios.append(promedio)
    return promedios

def obtener_mejor_trimestre(promedios):
    mayor = promedios[0]
    for i in range(len(promedios)):
        if promedios[i] > mayor:
            mayor = promedios[i]
    
    trimestres_ganadores = []
    for i in range(len(promedios)):
        if promedios[i] == mayor:
            trimestres_ganadores.append(i + 1)
    
    return trimestres_ganadores, mayor