import random

#>/ Funciones que no reciben parametros y no devuelven resultados.
def mostrar_bienvenida():
    #no hay parametros de entrada entre los parentesis
    print("¡hola bienvenida!")
    print ("por favor selecciona una opcion del manu")
    print("1.opcion 1")
    print("2.opcion 2")
    print("3.opcion 3")
    print("4.salida")

#para usar la funcion, se debe llamar a la funcion por su nombre seguido de parentesis.
mostrar_bienvenida()

#>/ Funciones que reciben parametros y no devuelven resultados.
def saludar_persona(nombre, edad):
    #recibe "nombre" y "edad" como parametros de entrada
    print(f"Hola {nombre}, veo que tienes {edad} años.")
    #no tiene return, solo en la pantalla el mensaje.

def tirar_dado():
    #no recibe parametros de entrada
    numero_obtenido = random.randint(1, 6)  # Genera un número aleatorio entre 1 y 6
    return numero_obtenido  # Devuelve el número obtenido al llamar a la función    

resultado = tirar_dado()  # llamamos a la funcion y guardamos el resultado en una variable
print(f"Has tirado un dado y obtuviste: {resultado}")#imprimimos el resultado

#>/ Funciones que no reciben parametros y devuelven resultados.

def calcula_area_rectangulo(base, altura):
    #recibir los datos necesarios
    area = base * altura  # Calcula el resultado del calculo
    #devuelve el resultado del calculo
    return area  

#para usarla:
mi_area=calcula_area_rectangulo(5, 10) 
print(f"El area del rectangulo es: {mi_area}") 