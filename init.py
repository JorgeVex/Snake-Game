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
azul = (0, 0, 255)
amarillo = (255, 255, 0)
naranja = (255, 165, 0)
morado = (128, 0, 128)
rosa = (255, 192, 203)
celeste = (0, 191, 255)
marron = (165, 42, 42)
gris = (128, 128, 128)

# Función para seleccionar el color de la serpiente
def seleccionar_color_serpiente():
    """
    Esta función muestra una paleta de colores en la pantalla, donde cada color es un cuadrado
    que el jugador puede seleccionar haciendo clic en él. La función espera hasta que el jugador
    haga clic en un color y devuelve el color seleccionado.
    """
    # Lista de colores disponibles para que el jugador elija
    colores = [verde, rojo, azul, amarillo, naranja, morado, rosa, celeste, marron, gris]
    
    # Definir las dimensiones de la paleta de colores
    ancho_cuadro = 50
    alto_cuadro = 50
    separacion = 10
    filas = 2
    columnas = len(colores) // filas
    
    # Calcular la posición de la paleta de colores en la pantalla
    x_inicial = (ancho - (columnas * ancho_cuadro + (columnas - 1) * separacion)) // 2
    y_inicial = (alto - (filas * alto_cuadro + (filas - 1) * separacion)) // 2
    
    # Mostrar la pregunta de selección de color
    fuente = pygame.font.SysFont("arial", 20)
    pregunta_texto = fuente.render("Selecciona un color para la serpiente:", True, blanco)
    rect_pregunta = pregunta_texto.get_rect(center=(ancho//2, y_inicial - 30))
    pantalla.blit(pregunta_texto, rect_pregunta)
    
    # Mostrar la paleta de colores en la pantalla
    for i, color in enumerate(colores):
        fila = i // columnas
        columna = i % columnas
        x = x_inicial + columna * (ancho_cuadro + separacion)
        y = y_inicial + fila * (alto_cuadro + separacion)
        pygame.draw.rect(pantalla, color, (x, y, ancho_cuadro, alto_cuadro))
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Esperar a que el jugador seleccione un color
    seleccionado = False
    while not seleccionado:
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Obtener la posición del clic del mouse
                x, y = pygame.mouse.get_pos()
                # Verificar si el clic está dentro de un cuadro de color
                for i in range(len(colores)):
                    fila = i // columnas
                    columna = i % columnas
                    x_cuadro = x_inicial + columna * (ancho_cuadro + separacion)
                    y_cuadro = y_inicial + fila * (alto_cuadro + separacion)
                    if x_cuadro <= x < x_cuadro + ancho_cuadro and y_cuadro <= y < y_cuadro + alto_cuadro:
                        return colores[i]

color_serpiente = seleccionar_color_serpiente()

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
        pygame.draw.rect(pantalla, color_serpiente, (pos[0], pos[1], 10, 10))

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
    fuente = pygame.font.SysFont("arial", 20)
    superficie_puntaje = fuente.render(" Puntaje: " + str(puntaje), True, blanco)
    rectangulo_puntaje = superficie_puntaje.get_rect()
    pantalla.blit(superficie_puntaje, rectangulo_puntaje)

# Función que se llama cuando el juego termina
def fin_juego():
    """
    Muestra un mensaje de "Game Over" en la pantalla y termina el juego.
    """
    fuente = pygame.font.SysFont("arial", 60)
    superficie_fin_juego = fuente.render("FIN DEL JUEGO", True, rojo)
    rectangulo_fin_juego = superficie_fin_juego.get_rect()
    rectangulo_fin_juego.midtop = (ancho / 2, alto / 4)
    pantalla.blit(superficie_fin_juego, rectangulo_fin_juego)
    pygame.display.flip()
    pygame.time.delay(5000)  # Pausa por 5000 milisegundos (5 segundos)
    pygame.quit()
    quit()

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Si se cierra la ventana
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN: # Si se presiona una tecla
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                if direccion_serpiente != "ABAJO":
                    cambio_direccion = "ARRIBA"
            elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                if direccion_serpiente != "ARRIBA":
                    cambio_direccion = "ABAJO"
            elif evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                if direccion_serpiente != "DERECHA":
                    cambio_direccion = "IZQUIERDA"
            elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
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
