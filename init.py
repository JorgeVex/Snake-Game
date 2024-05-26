import pygame
import random

# print("Pygame version:", pygame.__version__)

# Inicializar pygame
pygame.init()

# Configurar la pantalla
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Posición inicial y dirección de la serpiente
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction

# Posición de la comida
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

# Puntaje
score = 0

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, green, (pos[0], pos[1], 10, 10))

def draw_food(food_pos):
    pygame.draw.rect(screen, white, (food_pos[0], food_pos[1], 10, 10))

def update_score(score):
    font = pygame.font.SysFont("arial", 30)
    score_surface = font.render("Score: " + str(score), True, white)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

def game_over():
    font = pygame.font.SysFont("arial", 60)
    game_over_surface = font.render("Game Over", True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.quit()
    quit()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake_direction != "DOWN":
                    change_to = "UP"
            elif event.key == pygame.K_DOWN:
                if snake_direction != "UP":
                    change_to = "DOWN"
            elif event.key == pygame.K_LEFT:
                if snake_direction != "RIGHT":
                    change_to = "LEFT"
            elif event.key == pygame.K_RIGHT:
                if snake_direction != "LEFT":
                    change_to = "RIGHT"

    # Actualizar la dirección de la serpiente
    snake_direction = change_to

    # Actualizar la posición de la serpiente según la dirección
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10

    # Mecanismo para que la serpiente crezca
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Generar comida en una nueva posición aleatoria
    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    food_spawn = True

    # Verificar condiciones de fin de juego
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        game_over()
    for segment in snake_body[1:]:
        if snake_pos[0] == segment[0] and snake_pos[1] == segment[1]:
            game_over()

    # Limpiar la pantalla y dibujar los elementos
    screen.fill(black)
    draw_snake(snake_body)
    draw_food(food_pos)
    update_score(score)

    pygame.display.flip()

    # Controlar la velocidad del juego
    clock.tick(10)