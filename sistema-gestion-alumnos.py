from random import choice

# Inicializacion de diccionario de datos
datos_alumnos = []

# Inicializacion de variables
opcion = 0
identificacion_estudiante = ''
nombre_estudiante = ''
edad_estudiante = 0
genero_estudiante = ''
promedio_estudiante = 0
estudiante = None

# funciones auxiliares
def buscar_estudiante(identificador:str, filtro:str) -> dict:
    
    # Recorre la lista de los datos de alumnos
    for i in datos_alumnos:
        if i[filtro] == identificador.lower():
            print(i)
            # Retorna el diccionario
            return i
        
    # Retorna un diccionario vacio si no se encontro ninguna coincidencia     
    return {}
    
    
    """if filtro == 'nombre':
        
        
    elif filtro == 'codigo':
        for i in datos_alumnos:
            if i['codigo'] == identificador:
                #retorna el diccionario
                return i
        # Retorna un diccionario vacio si no se encontro ninguna coincidencia
        return {}"""

def generar_codigo_estudiante() -> str:
    """Genera codigo identificacion de estudiante"""
    
    secuencia_alfanumerica = 'abcdefghijklmnñopqrstuvwxyz0123456789'
    identificacion_estudiante = ''
    
    for i in range(7):
        valor = choice(secuencia_alfanumerica)
        identificacion_estudiante += valor
        
    return identificacion_estudiante
   
def validar_opcion(texto:str):
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

def validar_datos_estudiante() -> dict:
    try:
        nombre_estudiante = input('Nombre: ').lower()
        
        # valida que el estudiante no existe:
        exite_estudiante = buscar_estudiante(nombre_estudiante, 'nombre')
        if exite_estudiante != {}:
            print('Error: el nombre de estudiante ya existe.')
            return {}
        
        edad_estudiante = int(input('Edad (entre 12 y 80 años): '))
        
        # valida si al edad esta fuera del rango de edad (12 - 80)
        if edad_estudiante < 12 or edad_estudiante > 80:
            print('Error: edad ingresada invalida, esta fuera del rango de edades (12 - 80)')
            return {}
        
        genero_estudiante = input('Genero (solo "F" o "M"): ').upper()
        
        # valida que el genero este dentro del rango (F y M)
        if genero_estudiante != 'F' and genero_estudiante != 'M':
            print('Error: solo se permiten "F" de femenino o "M" de masculino.') 
            return {}
        
        promedio_estudiante = float(input('Promedio de notas (entre 1.0 y 7.0): '))
        
        # valida que la nota este dentro del rango (1.0 y 7.0)
        if promedio_estudiante < 1.0 or promedio_estudiante > 7.0:
            print('Error: promedio invalido, solo se permiten notas entre 1.0 y 7.0')
            return {}
        
        # Retorna un diccionario con todos los datos del estudiante
        return {"nombre":nombre_estudiante, "edad":edad_estudiante, "genero":genero_estudiante, "promedio":promedio_estudiante}
    
    except ValueError:
        print('Error: algun valor ingresado invalido.')
        return {}

def crear_estudiante() -> None:
    estudiante = validar_datos_estudiante()
    codigo_unico_estudiante = generar_codigo_estudiante()
    
    # Si el diccionario de estudiante es diferente a un diccioanrio vacia, entra.
    if estudiante != {}:
        estudiante['codigo'] = codigo_unico_estudiante
        datos_alumnos.append(estudiante)
        print('¡Estudiante agregado con exito!')


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
        crear_estudiante()
    elif opcion == 2:
        print('')
        