from funciones import *
from inputs import *
from archivos import *
from prints import *

def iniciar_menu():
    alumnos = []
    datos_cargados = False

    while True:
        print("=== MENU ===")
        print("1. Cargar alumnos")
        print("2. Mostrar egresados por plan")
        print("3. Mostrar egresados anteriores al año 2000")
        print("4. Buscar alumno por nombre o apellido")
        print("5. Salon de la fama")
        print("6. Salir")

        opcion = pedir_opcion("Seleccione una opción: ", 1, 6)

        match opcion:
            case 1:
                print("1. Cargar desde archivo")
                print("2. Carga manual")
                sub_opcion = pedir_opcion("Seleccione: ", 1, 2)
                if sub_opcion == 1:
                    alumnos = cargar_desde_json()
                else:
                    cargar_manual(alumnos)
                datos_cargados = True
                print("Datos cargados correctamente!")
            case 2:
                if datos_cargados:
                    plan = pedir_plan("Ingrese plan (1991, 2003, 2024): ")
                    egresados = obtener_egresados_por_plan(alumnos, plan)
                    mostrar_egresados(egresados)
                else:
                    print("Primero debe cargar los datos")
            case 3:
                if datos_cargados:
                    resultado = obtener_egresados_anteriores_2000(alumnos)
                    if len(resultado) > 0:
                        promedio = calcular_promedio_general(resultado)
                    else:
                        promedio = 0
                    mostrar_egresados_anteriores_2000(resultado, promedio)
                else:
                    print("Primero debe cargar los datos")
            case 4:
                if datos_cargados:
                    texto = pedir_nombre("Ingrese nombre o apellido a buscar: ")
                    resultado = buscar_por_nombre_o_apellido(alumnos, texto)
                    mostrar_busqueda(resultado)
                else:
                    print("Primero debe cargar los datos")
            case 5:
                if datos_cargados:
                    salon = obtener_salon_de_la_fama(alumnos)
                    salon = ordenar_por_nota(salon)
                    mostrar_salon_de_la_fama(salon)
                else:
                    print("Primero debe cargar los datos")
            case 6:
                guardar_json(alumnos)
                print("Saliendo...")
                break