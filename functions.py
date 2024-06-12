import pygame
from colors import *

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
