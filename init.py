import pygame
import random

# print("Pygame version:", pygame.__version__)

# Inicializar pygame
pygame.init()

# Configurar la pantalla
ancho, alto = 640, 480
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de la Serpiente")

# Colores (definidos en formato RGB)
negro = (0, 0, 0)
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)

# Posición inicial y dirección de la serpiente
pos_serpiente = [100, 50] # Coordenadas iniciales de la cabeza de la serpiente
cuerpo_serpiente = [[100, 50], [90, 50], [80, 50]] # Segmentos iniciales del cuerpo de la serpiente
direccion_serpiente = "DERECHA" # Dirección inicial de movimiento
cambio_direccion = direccion_serpiente # Variable para cambiar la dirección

# Posición de la comida (generada aleatoriamente)
pos_comida = [random.randrange(1, (ancho//10)) * 10, random.randrange(1, (alto//10)) * 10]
comida_spawn = True # Indica si la comida está en pantalla

# Puntaje
puntaje = 0

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Función para dibujar la serpiente en pantalla
def dibujar_serpiente(cuerpo_serpiente):
    """
    Dibuja cada segmento de la serpiente en la pantalla.

    Argumentos:
    snake_body -- Lista de posiciones (coordenadas x, y) de cada segmento del cuerpo de la serpiente
    """
    for pos in cuerpo_serpiente:
        pygame.draw.rect(pantalla, verde, (pos[0], pos[1], 10, 10))

# Función para dibujar la comida en pantalla
def dibujar_comida(pos_comida):
    """
    Dibuja la comida en la pantalla.

    Argumentos:
    food_pos -- Posición (coordenadas x, y) de la comida
    """
    pygame.draw.rect(pantalla, blanco, (pos_comida[0], pos_comida[1], 10, 10))

# Función para actualizar y mostrar el puntaje en pantalla
def actualizar_puntaje(puntaje):
    """
    Actualiza y muestra el puntaje actual en la pantalla.

    Argumentos:
    puntaje -- El puntaje actual del jugador
    """
    fuente = pygame.font.SysFont("arial", 30)
    superficie_puntaje = fuente.render("Puntaje: " + str(puntaje), True, blanco)
    rectangulo_puntaje = superficie_puntaje.get_rect()
    pantalla.blit(superficie_puntaje, rectangulo_puntaje)

# Función que se llama cuando el juego termina
def fin_juego():
    """
    Muestra un mensaje de "Game Over" en la pantalla y termina el juego.
    """
    fuente = pygame.font.SysFont("arial", 60)
    superficie_fin_juego = fuente.render("Fin del Juego", True, rojo)
    rectangulo_fin_juego = superficie_fin_juego.get_rect()
    rectangulo_fin_juego.midtop = (ancho / 2, alto / 4)
    pantalla.blit(superficie_fin_juego, rectangulo_fin_juego)
    pygame.display.flip()
    pygame.quit()
    quit()

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Si se cierra la ventana
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN: # Si se presiona una tecla
            if evento.key == pygame.K_UP:
                if direccion_serpiente != "ABAJO":
                    cambio_direccion = "ARRIBA"
            elif evento.key == pygame.K_DOWN:
                if direccion_serpiente != "ARRIBA":
                    cambio_direccion = "ABAJO"
            elif evento.key == pygame.K_LEFT:
                if direccion_serpiente != "DERECHA":
                    cambio_direccion = "IZQUIERDA"
            elif evento.key == pygame.K_RIGHT:
                if direccion_serpiente != "IZQUIERDA":
                    cambio_direccion = "DERECHA"

    # Actualizar la dirección de la serpiente
    direccion_serpiente = cambio_direccion

    # Actualizar la posición de la serpiente según la dirección
    if direccion_serpiente == "ARRIBA":
        pos_serpiente[1] -= 10
    elif direccion_serpiente == "ABAJO":
        pos_serpiente[1] += 10
    elif direccion_serpiente == "IZQUIERDA":
        pos_serpiente[0] -= 10
    elif direccion_serpiente == "DERECHA":
        pos_serpiente[0] += 10
        
    # Hacer que la serpiente atraviese los bordes
    if pos_serpiente[0] < 0:
        pos_serpiente[0] = ancho - 10
    elif pos_serpiente[0] >= ancho:
        pos_serpiente[0] = 0
    if pos_serpiente[1] < 0:
        pos_serpiente[1] = alto - 10
    elif pos_serpiente[1] >= alto:
        pos_serpiente[1] = 0

    # Mecanismo para que la serpiente crezca
    cuerpo_serpiente.insert(0, list(pos_serpiente)) # Insertar una copia de la nueva posición de la cabeza al inicio del cuerpo de la serpiente
    if pos_serpiente[0] == pos_comida[0] and pos_serpiente[1] == pos_comida[1]: # Si la serpiente come la comida
        puntaje += 1
        comida_spawn = False # Se necesitará generar nueva comida
    else:
        cuerpo_serpiente.pop() # Eliminar el último segmento del cuerpo de la serpiente si no ha comido

    # Generar comida en una nueva posición aleatoria si no hay comida en pantalla
    if not comida_spawn:
        pos_comida = [random.randrange(1, (ancho//10)) * 10, random.randrange(1, (alto//10)) * 10]
    comida_spawn = True

    # Verificar condiciones de fin de juego
    if pos_serpiente[0] < 0 or pos_serpiente[0] >= ancho or pos_serpiente[1] < 0 or pos_serpiente[1] >= alto:
        fin_juego()
    for segmento in cuerpo_serpiente[1:]: # Verificar colisión con el propio cuerpo
        if pos_serpiente[0] == segmento[0] and pos_serpiente[1] == segmento[1]:
            fin_juego()

    # Limpiar la pantalla y dibujar los elementos
    pantalla.fill(negro) # Llenar la pantalla con color negro
    dibujar_serpiente(cuerpo_serpiente) # Dibujar la serpiente
    dibujar_comida(pos_comida) # Dibujar la comida
    actualizar_puntaje(puntaje) # Actualizar y mostrar el puntaje

    pygame.display.flip() # Actualizar la pantalla

    # Controlar la velocidad del juego
    reloj.tick(10) # Establecer la cantidad de cuadros por segundo (FPS)
