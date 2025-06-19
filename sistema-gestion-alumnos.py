from random import 

# Inicializacion de diccionario de datos
datos_alumnos = [{}]

# Inicializacion de variables
opcion = 0

# funciones auxiliares
def buscar_estudiante(identificador) -> dict:
    print('Buscar estudiante')

def generar_codigo_estudiante() -> str:
    print('Genera codigo identificacion de estudiante')

def validar_opcion(texto):
    while True:
        try:
            opcion = int(input(texto))
            
            # Verifica que la opcion ingresada este dentro del rango de opciones
            if opcion < 1 or opcion > 6:
                print('Error: el valor ingresado esta fuera del rango del opciones.')
                continue
            
            # retorna el numero de la opcion
            return opcion

        except ValueError:
            print('Error: solamente se permiten numeros enteros.')



while True:    
    print("""
*********************************
Sistema de Gestión de Estudiantes
1) Registrar estudiante
2) Buscar estudiante
3) Modificar datos de estudiante
4) Eliminar estudiante
5) Mostrar todos los estudiantes
6) Salir
*********************************""")
    
    opcion = validar_opcion('Ingrese la opcion: ')
    
    if opcion == 1:

    