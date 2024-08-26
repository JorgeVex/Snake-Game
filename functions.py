import pygame
import random
import time
from conf.colors import *

def seleccionar_color_serpiente(pantalla, ANCHO, ALTO):
    """
    Muestra una paleta de colores para seleccionar el color de la serpiente.
    
    Argumentos:
    pantalla -- Pantalla de juego.
    ANCHO -- Ancho de la pantalla.
    ALTO -- Alto de la pantalla.
    
    Retorna:
    color seleccionado.
    """
    colores = [VERDE, ROJO, AZUL, AMARILLO, NARANJA, MORADO, ROSA, CELESTE, MARRON, GRIS]
    
    ancho_cuadro = 50
    alto_cuadro = 50
    separacion = 10
    filas = 2
    columnas = len(colores) // filas
    
    x_inicial = (ANCHO - (columnas * ancho_cuadro + (columnas - 1) * separacion)) // 2
    y_inicial = (ALTO - (filas * alto_cuadro + (filas - 1) * separacion)) // 2
    
    fuente = pygame.font.SysFont("arial", 20)
    pregunta_texto = fuente.render("Selecciona un color para la serpiente:", True, BLANCO)
    rect_pregunta = pregunta_texto.get_rect(center=(ANCHO//2, y_inicial - 30))
    pantalla.blit(pregunta_texto, rect_pregunta)
    
    for i, color in enumerate(colores):
        fila = i // columnas
        columna = i % columnas
        x = x_inicial + columna * (ancho_cuadro + separacion)
        y = y_inicial + fila * (alto_cuadro + separacion)
        pygame.draw.rect(pantalla, color, (x, y, ancho_cuadro, alto_cuadro))
    
    pygame.display.flip()
    
    seleccionado = False
    while not seleccionado:
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for i in range(len(colores)):
                    fila = i // columnas
                    columna = i % columnas
                    x_cuadro = x_inicial + columna * (ancho_cuadro + separacion)
                    y_cuadro = y_inicial + fila * (alto_cuadro + separacion)
                    if x_cuadro <= x < x_cuadro + ancho_cuadro and y_cuadro <= y < y_cuadro + alto_cuadro:
                        return colores[i]

def dibujar_serpiente(pantalla, cuerpo_serpiente, color_serpiente):
    """
    Dibuja la serpiente en la pantalla.
    
    Argumentos:
    pantalla -- Pantalla de juego.
    cuerpo_serpiente -- Lista de posiciones de la serpiente.
    color_serpiente -- Color de la serpiente.
    """
    for pos in cuerpo_serpiente:
        pygame.draw.rect(pantalla, color_serpiente, (pos[0], pos[1], 10, 10))

def dibujar_comida(pantalla, pos_comida):
    """
    Dibuja la comida en la pantalla.
    
    Argumentos:
    pantalla -- Pantalla de juego.
    pos_comida -- Posición de la comida.
    """
    pygame.draw.rect(pantalla, BLANCO, (pos_comida[0], pos_comida[1], 10, 10))

def actualizar_puntaje(pantalla, puntaje, ANCHO):
    """
    Actualiza y muestra el puntaje en la pantalla.
    
    Argumentos:
    pantalla -- Pantalla de juego.
    puntaje -- Puntaje actual.
    ANCHO -- Ancho de la pantalla.
    """
    fuente = pygame.font.SysFont("arial", 20)
    superficie_puntaje = fuente.render(" Puntaje: " + str(puntaje), True, BLANCO)
    rectangulo_puntaje = superficie_puntaje.get_rect()
    pantalla.blit(superficie_puntaje, rectangulo_puntaje)

def generar_obstaculos(num_obstaculos, ANCHO, ALTO, tamaño):
    """
    Genera una lista de posiciones de obstáculos aleatorios.

    Argumentos:
    num_obstaculos -- Número de obstáculos a generar
    ANCHO -- Ancho de la pantalla
    ALTO -- Alto de la pantalla
    tamaño -- Tamaño del lado del cuadrado del obstáculo

    Retorna:
    Una lista de posiciones (coordenadas x, y) de los obstáculos.
    """
    obstaculos = []
    for _ in range(num_obstaculos):
        x = random.randrange(1, (ANCHO // tamaño)) * tamaño
        y = random.randrange(1, (ALTO // tamaño)) * tamaño
        obstaculos.append([x, y])
    return obstaculos

def dibujar_obstaculos(pantalla, obstaculos, color):
    """
    Dibuja los obstáculos en la pantalla.

    Argumentos:
    pantalla -- Superficie de Pygame donde se dibujarán los obstáculos
    obstaculos -- Lista de posiciones (coordenadas x, y) de los obstáculos
    color -- Color de los obstáculos
    """
    for pos in obstaculos:
        pygame.draw.rect(pantalla, color, (pos[0], pos[1], 10, 10))
        
def agregar_potenciador(pantalla, pos_potenciador):
    """
    Dibuja el potenciador en la pantalla.
    
    Argumentos:
    pantalla -- Pantalla de juego.
    pos_potenciador -- Posición del potenciador.
    """
    pygame.draw.circle(pantalla, ROJO, pos_potenciador, 10)
    
def generar_potenciador(ANCHO, ALTO):
    """
    Genera una posición aleatoria para el potenciador.
    
    Argumentos:
    ANCHO -- Ancho de la pantalla.
    ALTO -- Alto de la pantalla.
    
    Retorna:
    Posición del potenciador.
    """
    return [random.randrange(1, (ANCHO // 10)) * 10, random.randrange(1, (ALTO // 10)) * 10]

        
def fin_juego(pantalla, ANCHO, ALTO):
    """
    Muestra un mensaje de "Game Over" en la pantalla y termina el juego.
    
    Argumentos:
    pantalla -- Pantalla de juego.
    ANCHO -- Ancho de la pantalla.
    ALTO -- Alto de la pantalla.
    """
    fuente = pygame.font.SysFont("arial", 60)
    superficie_fin_juego = fuente.render("FIN DEL JUEGO", True, ROJO)
    rectangulo_fin_juego = superficie_fin_juego.get_rect()
    rectangulo_fin_juego.midtop = (ANCHO / 2, ALTO / 4)
    pantalla.blit(superficie_fin_juego, rectangulo_fin_juego)
    pygame.display.flip()
    pygame.time.delay(5000)
    pygame.quit()
    quit()