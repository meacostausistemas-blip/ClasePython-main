# Este programa es una calculadora de promedios escolares implementada con funciones. Permite ingresar materias y calificaciones, calcular promedios, clasificar en aprobadas/reprobadas y mostrar estadísticas.

# Función para ingresar calificaciones: solicita nombres de materias y calificaciones, valida entradas y retorna listas.
def ingresar_calificaciones():
    # Inicializar listas vacías para materias y calificaciones
    materias = []
    calificaciones = []
    # Bucle para ingresar múltiples materias
    while True:
        # Solicitar nombre de la materia y quitar espacios
        materia = input("Ingrese el nombre de la materia: ").strip()
        # Intentar convertir calificación a float y validar rango
        try:
            nota = float(input("Ingrese la calificación (0 a 10): "))
            # Verificar si está entre 0 y 10
            if nota < 0 or nota > 10:
                print("Error: la calificación debe estar entre 0 y 10.")
                continue
        except ValueError:
            # Manejar error si no es número
            print("Error: ingrese un número válido.")
            continue

        # Agregar a las listas
        materias.append(materia)
        calificaciones.append(nota)

        # Preguntar si continuar
        continuar = input("¿Desea ingresar otra materia? (s/n): ").lower()
        # Salir si no es 's'
        if continuar != "s":
            break
    # Retornar las listas
    return materias, calificaciones

# Función para calcular el promedio: recibe lista de calificaciones y devuelve el promedio.
def calcular_promedio(calificaciones):
    # Verificar si la lista está vacía para evitar división por cero
    if len(calificaciones) == 0:
        return 0
    # Calcular y retornar el promedio
    return sum(calificaciones) / len(calificaciones)

# Función para determinar estado: recibe calificaciones y umbral, retorna índices de aprobadas y reprobadas.
def determinar_estado(calificaciones, umbral=5.0):
    # Inicializar listas para índices
    aprobadas = []
    reprobadas = []
    # Iterar con enumerate para obtener índice y nota
    for i, nota in enumerate(calificaciones):
        # Clasificar según umbral
        if nota >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    # Retornar listas de índices
    return aprobadas, reprobadas

# Función para encontrar extremos: recibe calificaciones y retorna índices de max y min.
def encontrar_extremos(calificaciones):
    # Verificar si lista vacía
    if len(calificaciones) == 0:
        return None, None
    # Encontrar índices de max y min
    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))
    # Retornar índices
    return indice_max, indice_min

# Función principal: coordina el flujo del programa.
def main():
    # Llamar a función para ingresar datos
    materias, calificaciones = ingresar_calificaciones()

    # Verificar si se ingresaron datos
    if len(materias) == 0:
        print("No se ingresaron materias. Programa finalizado.")
        return

    # Calcular promedio usando la función
    promedio = calcular_promedio(calificaciones)
    # Determinar aprobadas y reprobadas
    aprobadas, reprobadas = determinar_estado(calificaciones)
    # Encontrar extremos
    indice_max, indice_min = encontrar_extremos(calificaciones)

    # Mostrar resumen
    print("\n--- RESUMEN FINAL ---")
    # Listar todas las materias
    for i in range(len(materias)):
        print(f"{materias[i]}: {calificaciones[i]}")

    # Mostrar promedio
    print(f"\nPromedio general: {promedio:.2f}")

    # Mostrar aprobadas
    print("\nMaterias aprobadas:")
    for i in aprobadas:
        print(f"{materias[i]} ({calificaciones[i]})")

    # Mostrar reprobadas
    print("\nMaterias reprobadas:")
    for i in reprobadas:
        print(f"{materias[i]} ({calificaciones[i]})")

    # Mostrar extremos si existen
    if indice_max is not None:
        print(f"\nMejor materia: {materias[indice_max]} ({calificaciones[indice_max]})")
        print(f"Peor materia: {materias[indice_min]} ({calificaciones[indice_min]})")

    # Mensaje de despedida
    print("\nGracias por usar la calculadora de promedios. ¡Hasta pronto!")

# Ejecutar main si el script se corre directamente
if __name__ == "__main__":
    main()


##Programa completo con funciones para calcular promedios escolares. Incluye validación de entradas, clasificación de materias y estadísticas finales. El programa se ejecuta a través de la función main(), que coordina el flujo general del programa.