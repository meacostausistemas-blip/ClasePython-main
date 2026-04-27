"""
reto de programacion simulador de probabilidades de la ruleta rusa

1.descripcion del problema:
se requiere desarrollar un programa de python que simule un sistema de azar basado en un revolver de seis recamaras. el programa debe gestionar eventos aleatorios, pausas de ejecucion para mejorar la experiencia de usuario y control de flujo basado en condiciones de victoria o derrota.

2. requisitos tecnicos

el algoritmo debe cumplir con los siguientes requisitos:

* inicializacion definir una recamara ganadora (bala) de forma aleatoria entre 1 y 6.

* bucle de juego: el usuario debe interactuar manualmente para girar el tambor y disparar.

* mecanica de azar: encada turno, la posicion de la de la recamara que queda al frente al percutor debe ser aleatoria, simulando el giro del tambor.

* concion de derrota: si la recamara seleccionada coincide con la de la bala, el programa termina inmediatamente.

* condicion de victoria: el jugador gana si logra sobrevivir a 5 intentos (ya que el sexto seria el intento fatal).

"""

import random, time 

print("="*50)
print("bienvenido al simulador de la ruleta rusa")
print("="*50)

input("poner bala en el tambor (presiona enter)")
bala = random.randint(1, 6)
time.sleep(0.5)

disparos = 0 #variable para contar los disparos realizados  

while True:
    input("girar el tambor (presiona enter)")
    recamara = random.randint(1, 6)

    input("apuntar y disparar (presiona enter)" )
    time.sleep(1)

    if recamara == bala:
        print("¡bang! has perdido. la bala estaba en la recamara numero", bala)
        break

    else:
        disparos += 1
        print("¡click! has sobrevivido a este intento.")
        print("intentos de disparo:", disparos)

        if disparos == 5:
            print("¡felicidades! has sobrevivido a 5 intentos y ganado el juego.")
            break

print("="*50)
print("fin del juego - gracias por jugar.")
print("="*50)


        
    