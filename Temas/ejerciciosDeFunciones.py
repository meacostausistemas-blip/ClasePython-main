'''
EJERCICIO DE PROGRAMACIÓN INTERMEDIA - FUNCIONES

El ejercicio consite en la implementación de una calculadora que permita realizar las siguientes 
operaciones: 

1. Sumar Dos Números
2. Restar Dos Números
3. Multiplicar Dos Números
4. Dividir Dos Números
5. Calcular el factorial de un número
6. Calcular la potencia de un número elevado a otro

Para la implementación del ejercicio vamos a utilizar las siguientes funciones:

Función Sumar: se encargará de realizar todo el proceso de suma, incluyendo la solicitud de los 
dos números al usuario que se van a sumar.

Función Restar: se encargará de realizar todo el proceso de resta, incluyendo la solicitud del minuendo
y el sustraendo al usuario.

Función Multiplicar: se encargará de realizar todo el proceso de multiplicación, incluyendo la solicitud
de los factores al usuario.

Función Dividir: se encargará de realizar todo el proceso de división, incluyendo la solicitud del dividendo
y el divisor al usuario. Validar que no se realice una división por cero.

Función Factorial: Se encargará de solicitar el número del que se quiere calcular el factorial.
Una Vez tenga el numero invocará a la función de calcular factorial, validar que el número sea positivo 
y entero.

Función FactorialCalculo: función recursiva que se realiza en el cálculo del factorial del número que 
recibe por parámetro.

Función Potencia: se encargará de solicitar la base y el exponente al usuario e invocará a la 
función de calcular potencia,validar que el exponente sea un número entero.

Función PotenciaCalculo: función recursiva que se realiza en el cálculo de la potencia de los números
pasados como parámetros.

Función Calculadora: función principal que se encargará de mostrar el menú de opciones al usuario, 
solicitar la opción deseada y llamar a la función correspondiente según la opción seleccionada. 
La función debe continuar mostrando el menú hasta que el usuario decida salir.

Importante: tanto el menú como los mensajes de solicitud de datos y resultados deben ser claros 
y amigables para el usuario, y se deben manejar adecuadamente los casos de error, como la división 
por cero o la entrada de datos no válidos.

Utilizar diseño de Interfaz de Usuario mediante la consola utilizando ASCII Art para hacer el menú 
más atractivo visualmente.
'''

def FactorialCalculo(n):
    if n == 0 or n == 1:
        return 1
    return n * FactorialCalculo(n - 1)

def PotenciaCalculo(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / PotenciaCalculo(base, -exp)
    return base * PotenciaCalculo(base, exp - 1)

def Sumar():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La suma de {num1} y {num2} es: {num1 + num2}")
    except ValueError:
        print("Entrada inválida. Por favor ingrese números válidos.")

def Restar():
    try:
        minuendo = float(input("Ingrese el minuendo: "))
        sustraendo = float(input("Ingrese el sustraendo: "))
        print(f"La resta de {minuendo} menos {sustraendo} es: {minuendo - sustraendo}")
    except ValueError:
        print("Entrada inválida. Por favor ingrese números válidos.")

def Multiplicar():
    try:
        factor1 = float(input("Ingrese el primer factor: "))
        factor2 = float(input("Ingrese el segundo factor: "))
        print(f"El producto de {factor1} y {factor2} es: {factor1 * factor2}")
    except ValueError:
        print("Entrada inválida. Por favor ingrese números válidos.")

def Dividir():
    try:
        dividendo = float(input("Ingrese el dividendo: "))
        divisor = float(input("Ingrese el divisor: "))
        if divisor == 0:
            print("Error: No se puede dividir por cero.")
            return
        print(f"La división de {dividendo} entre {divisor} es: {dividendo / divisor}")
    except ValueError:
        print("Entrada inválida. Por favor ingrese números válidos.")

def Factorial():
    try:
        num = int(input("Ingrese un número entero positivo: "))
        if num < 0:
            print("El número debe ser positivo.")
            return
        result = FactorialCalculo(num)
        print(f"El factorial de {num} es: {result}")
    except ValueError:
        print("Entrada inválida. Debe ser un entero positivo.")

def Potencia():
    try:
        base = float(input("Ingrese la base: "))
        exp = int(input("Ingrese el exponente (entero no negativo): "))
        if exp < 0:
            print("El exponente debe ser no negativo.")
            return
        result = PotenciaCalculo(base, exp)
        print(f"{base} elevado a {exp} es: {result}")
    except ValueError:
        print("Entrada inválida. La base debe ser un número y el exponente un entero no negativo.")

def Calculadora():
    menu = """
   ____                _       _                 
  / ___|__ _ _ __ ___ | |__   / \\   ___ ___ ___  
 | |   / _` | '_ ` _ \\| '_ \\ / _ \\ / __/ __/ _ \\ 
 | |__| (_| | | | | | | |_) / ___ \\ (_| (_|  __/ 
  \\____\\__,_|_| |_| |_|_.__/_/   \\_\\___\\___\\___| 
                                                

Menú de Opciones:
1. Sumar Dos Números
2. Restar Dos Números
3. Multiplicar Dos Números
4. Dividir Dos Números
5. Calcular el Factorial de un Número
6. Calcular la Potencia de un Número
7. Salir
"""
    while True:
        print(menu)
        opcion = input("Seleccione una opción (1-7): ")
        if opcion == '1':
            Sumar()
        elif opcion == '2':
            Restar()
        elif opcion == '3':
            Multiplicar()
        elif opcion == '4':
            Dividir()
        elif opcion == '5':
            Factorial()
        elif opcion == '6':
            Potencia()
        elif opcion == '7':
            print("¡Gracias por usar la calculadora! Hasta luego.")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción del 1 al 7.")
        input("Presione Enter para continuar...")

if __name__ == "__main__":
    Calculadora()
