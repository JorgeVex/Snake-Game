import pygame

ANCHO, ALTO = 640, 480

DIRECCIONES = {
    pygame.K_UP: "ARRIBA",
    pygame.K_w: "ARRIBA",
    pygame.K_DOWN: "ABAJO",
    pygame.K_s: "ABAJO",
    pygame.K_LEFT: "IZQUIERDA",
    pygame.K_a: "IZQUIERDA",
    pygame.K_RIGHT: "DERECHA",
    pygame.K_d: "DERECHA"
}

OPPOSITE_DIRECTION = {
    "ARRIBA": "ABAJO",
    "ABAJO": "ARRIBA",
    "IZQUIERDA": "DERECHA",
    "DERECHA": "IZQUIERDA"
}
