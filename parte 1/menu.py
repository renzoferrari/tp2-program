from funciones import *
from inputs import *
from archivos import *
from prints import *

def iniciar_menu():
    matriz = []
    datos_cargados = False
    carga_manual = False
    
    while True:
        print("=== MENU ===")
        print("1. Cargar notas")
        print("2. Mostrar alumnos desaprobados")
        print("3. Mostrar alumnos con aplazos")
        print("4. Mostrar porcentaje de aprobados y desaprobados")
        print("5. Mostrar trimestre con mejor promedio")
        print("6. Salir")

        opcion = pedir_opcion("Seleccione una opción: ", 1, 6)

        match opcion:
            case 1:
                print("1. Carga manual")
                print("2. Cargar desde CSV")
                sub_opcion = pedir_opcion("Seleccione: ", 1, 2)
                if sub_opcion == 1:
                    matriz = cargar_notas_manual()
                    carga_manual = True
                else:
                    matriz = cargar_desde_csv()
                
                datos_cargados = True
                mostrar_matriz(matriz)
                print("Datos cargados correctamente!")
            case 2:
                 if datos_cargados:
                    desaprobados = obtener_desaprobados(matriz)
                    mostrar_desaprobados(matriz, desaprobados)
            case 3:
                if datos_cargados:
                    aplazados = obtener_aplazados(matriz)
                    mostrar_aplazados(matriz, aplazados)
                else:
                    print("Primero debe cargar los datos")
            case 4:
                if datos_cargados:
                    porcentaje_aprobados, porcentaje_desaprobados = calcular_porcentaje_aprobados(matriz)
                    mostrar_porcentajes(porcentaje_aprobados, porcentaje_desaprobados)
                else:
                    print("Primero debe cargar los datos")
            case 5:
                  if datos_cargados:
                      promedios = calcular_promedios_trimestres(matriz)
                      trimestres_ganadores, mayor = obtener_mejor_trimestre(promedios)
                      mostrar_mejor_trimestre(trimestres_ganadores, mayor)
                  else:
                      print("Primero debe cargar los datos")
            case 6:
                if carga_manual:
                    nombre = guardar_csv(matriz)
                    print("Archivo guardado como: " + nombre)
                print("Saliendo...")
                break