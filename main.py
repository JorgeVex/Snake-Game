import pygame
import random
import time
from conf.config import *
from conf.colors import *
from functions import seleccionar_color_serpiente, dibujar_serpiente, dibujar_comida, actualizar_puntaje, fin_juego, generar_obstaculos, dibujar_obstaculos, agregar_potenciador, generar_potenciador

# Inicializar pygame
pygame.init()

# Configurar la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Serpiente")

# Seleccionar color de la serpiente
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

# Variables del potenciador
puntos_potenciador = 9
potenciador_activado = False
velocidad_inicial = 10
velocidad_actual = velocidad_inicial
pos_potenciador = None
inicio_tiempo_potenciador = 0
tiempo_potenciador_duracion = 10000

# Generar obstáculos
num_obstaculos = 10
obstaculos = generar_obstaculos(num_obstaculos, ANCHO, ALTO, 10)

# Bucle principal del juego
while True:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key in DIRECCIONES:
                nueva_direccion = DIRECCIONES[evento.key]
                if nueva_direccion != OPPOSITE_DIRECTION[direccion_serpiente]:
                    cambio_direccion = nueva_direccion

    # Actualizar dirección de la serpiente
    direccion_serpiente = cambio_direccion

    # Mover la serpiente
    if direccion_serpiente == "ARRIBA":
        pos_serpiente[1] -= 10
    elif direccion_serpiente == "ABAJO":
        pos_serpiente[1] += 10
    elif direccion_serpiente == "IZQUIERDA":
        pos_serpiente[0] -= 10
    elif direccion_serpiente == "DERECHA":
        pos_serpiente[0] += 10
        
    # Atravesar los bordes
    if pos_serpiente[0] < 0:
        pos_serpiente[0] = ANCHO - 10
    elif pos_serpiente[0] >= ANCHO:
        pos_serpiente[0] = 0
    if pos_serpiente[1] < 0:
        pos_serpiente[1] = ALTO - 10
    elif pos_serpiente[1] >= ALTO:
        pos_serpiente[1] = 0

    # Actualizar el cuerpo de la serpiente
    cuerpo_serpiente.insert(0, list(pos_serpiente))
    if pos_serpiente == pos_comida:
        puntaje += 1
        comida_spawn = False
        
        # Activar el potenciador si el puntaje es múltiplo de 9
        if puntaje % puntos_potenciador == 0:
            potenciador_activado = True
            pos_potenciador = generar_potenciador(ANCHO, ALTO)
            # Restablecer la velocidad a la velocidad inicial al consumir el potenciador
            velocidad_actual = velocidad_inicial
            # Registrar el tiempo de inicio del potenciador
            inicio_tiempo_potenciador = pygame.time.get_ticks()
    else:
        cuerpo_serpiente.pop()

    # Generar nueva comida si no hay en pantalla
    if not comida_spawn:
        pos_comida = [random.randrange(1, (ANCHO//10)) * 10, random.randrange(1, (ALTO//10)) * 10]
    comida_spawn = True

    # Verificar colisiones con el potenciador
    if potenciador_activado and pos_serpiente == pos_potenciador:
        potenciador_activado = False
        obstaculos = generar_obstaculos(num_obstaculos, ANCHO, ALTO, 10)  # Cambia la posición de los obstáculos de forma aleatoria
        velocidad_actual = velocidad_inicial * 2  # Aumentar la velocidad
        inicio_tiempo_potenciador = pygame.time.get_ticks()  # Registrar el tiempo de inicio del potenciador
        
    # Verificar colisiones
    if pos_serpiente in cuerpo_serpiente[1:]:
        fin_juego(pantalla, ANCHO, ALTO)
    
    # Verifica las colisiones de la serpiente con cada obstaculo
    if pos_serpiente in obstaculos:
        fin_juego(pantalla, ANCHO, ALTO)
    for segmento in cuerpo_serpiente[1:]:
        if pos_serpiente[0] == segmento[0] and pos_serpiente[1] == segmento[1]:
            fin_juego(pantalla, ANCHO, ALTO)

    # Controlar la duración del potenciador
    if velocidad_actual > velocidad_inicial and pygame.time.get_ticks() - inicio_tiempo_potenciador > tiempo_potenciador_duracion:
        velocidad_actual = velocidad_inicial  # Restablecer la velocidad
    
    # Dibujar elementos en pantalla
    pantalla.fill(NEGRO)
    dibujar_serpiente(pantalla, cuerpo_serpiente, color_serpiente)
    dibujar_comida(pantalla, pos_comida)
    
    # Dibujar potenciador si está activado
    if potenciador_activado:
        agregar_potenciador(pantalla, pos_potenciador)
    
    actualizar_puntaje(pantalla, puntaje, ANCHO)
    dibujar_obstaculos(pantalla, obstaculos, AMARILLO)

    pygame.display.flip()

    # Controlar la velocidad del juego
    reloj.tick(velocidad_actual)
