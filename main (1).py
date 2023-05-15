import pygame # Importamos el módulo pygame para poder crear nuestro juego
import random # Importamos el módulo random para generar la posición aleatoria de la comida
pygame.init() # Inicializamos pygame
 # Definimos algunos colores usando la notación RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Configurar el tamaño de la pantalla
WINDOW_WIDTH = 600 #Definimos el ancho de la ventana
WINDOW_HEIGHT = 400 # Definimos la altura de la ventana
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
 
# Crear la ventana
pygame.display.set_caption('Snake Game') # Establecemos el título de la ventana
screen = pygame.display.set_mode(WINDOW_SIZE) # Creamos la ventana del juego con el tamaño especificado
clock = pygame.time.Clock()
FPS = 20
# Definimos el tamaño de los bloques de la serpiente y la velocidad del juego
BLOCK_SIZE = 10
snake_speed = 5
# Creamos una fuente para mostrar el puntaje en pantalla
font = pygame.font.SysFont(None, 25)
# Definimos una función para dibujar la serpiente
def snake(block_size, snakeList):
    for element in snakeList:
        pygame.draw.rect(screen, GREEN, [element[0], element[1], block_size, block_size])
# Función que muestra el mensaje en la pantalla
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [WINDOW_WIDTH/6, WINDOW_HEIGHT/3])
 
# Función principal del juego
def gameLoop():
    game_over = False
    game_close = False
 
    # Inicializar la posición de la serpiente
    x1 = WINDOW_WIDTH/2
    y1 = WINDOW_HEIGHT/2
 
    # Inicializar el cambio de posición de la serpiente
    x1_change = 0       
    y1_change = 0
 
    # Crear la lista de la serpiente
    snakeList = []
    Length_of_snake = 1
 
    # Crear la posición aleatoria de la comida
    foodx = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    foody = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
 
    # Bucle principal del juego
    while not game_over:
 
        # Si el juego se cierra
        while game_close == True:
            screen.fill(BLACK)
            message_to_screen("Perdiste! Presiona Q para salir o C para jugar de nuevo", RED)
            pygame.display.update()
 
            # Revisar la tecla presionada
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        # Detectar los eventos del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_speed
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_speed
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_speed
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_speed
                    x1_change = 0
 
        # Verificar si la serpiente choca con los bordes
        if x1 >= WINDOW_WIDTH or x1 < 0 or y1 >= WINDOW_HEIGHT or y1 < 0:
            game_close = True
 
        # Actualizar la posición de la serpiente
        x1 += x1_change
        y1 += y1_change
 
        # Dibujar la comida y la serpiente en la pantalla
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
 
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)
        if len(snakeList) > Length_of_snake:
            del snakeList[0]
 
        for segment in snakeList[:-1]:
            if segment == snakeHead:
                game_close = True
 
        snake(BLOCK_SIZE, snakeList)
        pygame.display.update()
 
        # Verificar si la serpiente se come la comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            foody = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            Length_of_snake += 1
 
        # Mostrar el puntaje
        score = Length_of_snake - 1
        score_font = font.render("Puntaje: " + str(score), True, WHITE)
        screen.blit(score_font, [0, 0])
 
        # Actualizar el juego
        pygame.display.update()
 
        # Configurar la velocidad de fotogramas
        clock.tick(FPS)
 
    # Cerrar el juego
    pygame.quit()
    quit()
 
# Iniciar el juego
gameLoop()