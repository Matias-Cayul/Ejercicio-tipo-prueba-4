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
            # Retorna el diccionario
            return i
        
    # Retorna un diccionario vacio si no se encontro ninguna coincidencia     
    return {}

def generar_codigo_estudiante() -> str:
    """Genera codigo identificacion de estudiante"""
    
    secuencia_alfanumerica = 'abcdefghijklmnñopqrstuvwxyz0123456789'
    identificacion_estudiante = ''
    
    for i in range(7):
        valor = choice(secuencia_alfanumerica)
        identificacion_estudiante += valor
        
    return identificacion_estudiante
   
def validar_opcion(texto:str, rango_minimo:int, rango_maximo:int):
    while True:
        try:
            opcion = int(input(texto))
            
            # Verifica que la opcion ingresada este dentro del rango de opciones
            if opcion < rango_minimo or opcion > rango_maximo:
                print('Error: el valor ingresado esta fuera del rango del opciones.')
                continue
            
            # retorna el numero de la opcion
            return opcion

        except ValueError:
            print('Error: solamente se permiten numeros enteros.')

def eliminar_estudiante(estudiante:dict) -> None:
    datos_alumnos.remove(estudiante)
    print('Estudiante eliminado.')

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

def modificar_datos_estudiante(estudiante:dict):
    
    try:
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
    except ValueError:
        print('Error: ')
    
    

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
    
    opcion = validar_opcion('Ingrese la opcion: ', 1, 6)
    
    # Crear estudiante
    if opcion == 1:
        crear_estudiante()
    
    # Buscar estudiante
    elif opcion == 2:
        print('------- Buscar estudiante -------')
        print('1) Nombre estudiante')
        print('2) Codigo estudiante')
        print('3) Regresar')
        
        opcion = validar_opcion('Ingrese una opcion: ', 1, 3)
        
        # Regresa al menu principal
        if opcion == 3:
            continue
        
        # Busca estudiante por codigo
        elif opcion == 2:
            identificador_estudiante = input('Ingrese codigo estudiante: ')
            estudiante = buscar_estudiante(identificador_estudiante, 'codigo')
            
            if estudiante != {}:
                print(f'Nombre: {estudiante['nombre']} - Edad: {estudiante['edad']} - Genero: {estudiante['genero']} - Codigo: {estudiante['codigo']} - Promedio: {estudiante['promedio']}')
            else:
                print('Error: estudiante no encontrado.')
            
        
        # Busca estudiante por nombre
        elif opcion == 1:
            identificador_estudiante = input('Ingrese nombre estudiante: ')
            estudiante = buscar_estudiante(identificador_estudiante, 'nombre')
            
            if estudiante != {}:
                print(f'Nombre: {estudiante['nombre']} - Edad: {estudiante['edad']} - Genero: {estudiante['genero']} - Codigo: {estudiante['codigo']} - Promedio: {estudiante['promedio']}')
            else:
                print('Error: estudiante no encontrado.')

    # Editar datos estudiante
    elif opcion == 3:
        codigo_estudiante = input('Ingrese codigo de estudiante: ')
        estudiante = buscar_estudiante(codigo_estudiante, 'codigo')
        
        if estudiante != {}:
            estudiante = modificar_datos_estudiante(estudiante)
            
            # Si el valor de estudiante esta vacio
            if estudiante == {}:
                print('Error: ')
            else:
                print('exito')
        else:
            print('Error: estudiante no encontrado')
    
    
        