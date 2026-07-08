def pedir_nota(mensaje):
    while True:
        cadena = input(mensaje)
        
        if len(cadena) > 0:
            es_numero = True
            for i in range(len(cadena)):
                valor_ascii = ord(cadena[i])
                if valor_ascii < 48 or valor_ascii > 57:
                    es_numero = False
                    break
            
            if es_numero:
                numero = int(cadena)
                if numero >= 1 and numero <= 10:
                    return numero
                else:
                    print("Error: la nota debe estar entre 1 y 10")
            else:
                print("Error: ingresaste caracteres inválidos")
        else:
            print("Error: no puede estar vacío")

def pedir_opcion(mensaje, minimo, maximo):
    while True:
        cadena = input(mensaje)
        
        if len(cadena) > 0:
            es_numero = True
            for i in range(len(cadena)):
                valor_ascii = ord(cadena[i])
                if valor_ascii < 48 or valor_ascii > 57:
                    es_numero = False
                    break
            
            if es_numero:
                numero = int(cadena)
                if numero >= minimo and numero <= maximo:
                    return numero
                else:
                    print("Error: ingrese una opción entre " + str(minimo) + " y " + str(maximo))
            else:
                print("Error: ingresaste caracteres inválidos")
        else:
            print("Error: no puede estar vacío")

