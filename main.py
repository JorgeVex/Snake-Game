import pygame
import random
from config import *
from colors import *
from functions import seleccionar_color_serpiente, dibujar_serpiente, dibujar_comida, actualizar_puntaje, fin_juego

# Inicializar pygame
pygame.init()

# Configurar la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Serpiente")

color_serpiente = seleccionar_color_serpiente(pantalla, ANCHO, ALTO)

# Posición inicial y dirección de la serpiente
pos_serpiente = [100, 50]
cuerpo_serpiente = [[100, 50], [90, 50], [80, 50]]
direccion_serpiente = "DERECHA"
cambio_direccion = direccion_serpiente

# Posición de la comida (generada aleatoriamente)
pos_comida = [random.randrange(1, (ANCHO//10)) * 10, random.randrange(1, (ALTO//10)) * 10]
comida_spawn = True

# Puntaje
puntaje = 0

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key in DIRECCIONES:
                nueva_direccion = DIRECCIONES[evento.key]
                if nueva_direccion != OPPOSITE_DIRECTION[direccion_serpiente]:
                    cambio_direccion = nueva_direccion

    direccion_serpiente = cambio_direccion

    if direccion_serpiente == "ARRIBA":
        pos_serpiente[1] -= 10
    elif direccion_serpiente == "ABAJO":
        pos_serpiente[1] += 10
    elif direccion_serpiente == "IZQUIERDA":
        pos_serpiente[0] -= 10
    elif direccion_serpiente == "DERECHA":
        pos_serpiente[0] += 10
        
    if pos_serpiente[0] < 0:
        pos_serpiente[0] = ANCHO - 10
    elif pos_serpiente[0] >= ANCHO:
        pos_serpiente[0] = 0
    if pos_serpiente[1] < 0:
        pos_serpiente[1] = ALTO - 10
    elif pos_serpiente[1] >= ALTO:
        pos_serpiente[1] = 0

    cuerpo_serpiente.insert(0, list(pos_serpiente))
    if pos_serpiente == pos_comida:
        puntaje += 1
        comida_spawn = False
    else:
        cuerpo_serpiente.pop()

    if not comida_spawn:
        pos_comida = [random.randrange(1, (ANCHO//10)) * 10, random.randrange(1, (ALTO//10)) * 10]
    comida_spawn = True

    if pos_serpiente in cuerpo_serpiente[1:]:
        fin_juego(pantalla, ANCHO, ALTO)

    pantalla.fill(NEGRO)
    dibujar_serpiente(pantalla, cuerpo_serpiente, color_serpiente)
    dibujar_comida(pantalla, pos_comida)
    actualizar_puntaje(pantalla, puntaje, ANCHO)

    pygame.display.flip()

    reloj.tick(10)
