"""
Reto de programación: Piedra, Papel o Tijeras

1. Descripción del problema:
se solicita desarrollar un programa en python que permita a un usuario enfrentarse a la computadora en el clásico juego de piedra, papel o tijeras. 
el programa debe gestionar la entrada del usuario, generar una elección aleatoria para la computadora y determinar el resultado del juego (victoria, derrota o empate) basándose en las reglas tradicionales.

2. Requisitos técnicos:
el algoritmo debe estructurarse de la siguiente manera:

* interfaz visual: mostrar el encabezado decorativo utilizando metodos de cadena como .center() y multiplicacion de caracteres.

* entrada de datos: Solicitar al usuario su elección. El programa debe ser capaz de reconocer la entrada sin importar si 
se escribe en mayúsculas o minúsculas.

* Inteligencia Aleatoria: La computadora debe elegir una opción de una lista predefinida de opciones (Piedra, Papel, Tijera) 
de forma aleatoria utilizando el módulo random.

* Logica de comparación:

Implementar las condiciones necesarias para evaluar.

1. Empate: Ambas elecciones son iguales.
2. Victoria: El usuario vence a la PC (Priedra vence a Tijera, Tijera vence a Papel, Papel vence a Piedra).
3. Derrota: La PC vence al usuario.

* Control de Flujo: El juego debe repetirse indefinidamente dentro de un blucle hasta que el usuario decida escribir 
la palabra (Salir).

Solución del Ejercicio Propuesto    
'''
"""

import random

# Figuras ASCII
figuras = {
    "piedra": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "papel": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "tijeras": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Opciones
opciones = ["piedra", "papel", "tijeras"]

print("🎮 Bienvenido a Piedra, Papel o Tijeras 🎮")
usuario = input("Elige piedra, papel o tijeras: ").lower()
computadora = random.choice(opciones)

# Mostrar elecciones con figuras
print("\nTú elegiste:", usuario)
print(figuras[usuario])
print("La computadora eligió:", computadora)
print(figuras[computadora])

# Lógica del juego
if usuario == computadora:
    print("🤝 ¡Empate!")
elif (usuario == "piedra" and computadora == "tijeras") or \
     (usuario == "papel" and computadora == "piedra") or \
     (usuario == "tijeras" and computadora == "papel"):
    print("🏆 ¡Ganaste!")
else:
    print("💻 La computadora gana...")
