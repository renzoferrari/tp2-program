from funciones import *
from inputs import *
from archivos import *
from prints import *

def iniciar_menu() -> None:
    """
    Inicia el menu principal del programa.
    """
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
                    matriz = cargar_notas_manual(7)
                    carga_manual = True
                else:
                    matriz = cargar_desde_csv("notas.csv")
                datos_cargados = True
                mostrar_matriz(matriz)
                print("Datos cargados correctamente!")
            case 2:
                if datos_cargados:
                    desaprobados = obtener_alumnos_con_nota_menor(matriz, 7)
                    mostrar_alumnos(desaprobados, "No hay alumnos desaprobados", "=== ALUMNOS DESAPROBADOS ===")
                else:
                    print("Primero debe cargar los datos")
            case 3:
                if datos_cargados:
                    aplazados = obtener_alumnos_con_nota_menor(matriz, 4)
                    mostrar_alumnos(aplazados, "No hay alumnos con aplazos", "=== ALUMNOS CON APLAZOS ===")
                else:
                    print("Primero debe cargar los datos")
            case 4:
                if datos_cargados:
                    porcentaje_aprobados = calcular_porcentaje_aprobados(matriz)
                    porcentaje_desaprobados = calcular_porcentaje_desaprobados(matriz)
                    mostrar_porcentajes(porcentaje_aprobados, porcentaje_desaprobados)
                else:
                    print("Primero debe cargar los datos")
            case 5:
                if datos_cargados:
                    promedios = calcular_promedios_trimestres(matriz)
                    mayor = obtener_mayor_promedio(promedios)
                    trimestres_ganadores = obtener_trimestres_ganadores(promedios, mayor)
                    mostrar_mejor_trimestre(trimestres_ganadores, mayor)
                else:
                    print("Primero debe cargar los datos")
            case 6:
                if carga_manual:
                    nombre = guardar_csv(matriz, "trimestre1,trimestre2,trimestre3")
                    print("Archivo guardado como: " + nombre)
                print("Saliendo...")
                break