import pygame

# 1. Inicializar Pygame
# Siempre es el primer paso. Prepara los módulos internos.
pygame.init()

# 2. Configuración de la Pantalla
ANCHO = 800
ALTO = 600
# Creamos la ventana (Superficie principal)
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Primer Juego")

# Reloj para controlar la velocidad del juego (FPS)
reloj = pygame.time.Clock()

# Variable para controlar el bucle principal
corriendo = True
jugador_x = 100
jugador_y = 100
# 3. Bucle del Juego (Game Loop)
while corriendo:
    # --- Manejo de Eventos ---
    # Revisamos todo lo que ha pasado (teclas, ratón, cerrar ventana)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            # Si el usuario pulsa la X de la ventana
            corriendo = False

    # --- Lógica del Juego ---
    # Aquí calcularemos movimientos, choques, etc.
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador_x -= 5
    if teclas[pygame.K_RIGHT]:
        jugador_x += 5
    if teclas[pygame.K_UP]:
        jugador_y -= 5
    if teclas[pygame.K_DOWN]:
        jugador_y += 5
    # --- Dibujado ---
    # Limpiamos la pantalla (pintamos de negro, por defecto es negro pero es bueno ser explícito)
    #pantalla.fill((0, 0, 0))  # RGB: (0, 0, 0) es Negro
    pygame.draw.rect(pantalla, (255, 0, 0), (jugador_x, jugador_y, 50, 50))
    # Actualizamos la pantalla para mostrar lo que hemos dibujado
    pygame.display.flip()

    # Controlamos los FPS (60 imágenes por segundo)
    reloj.tick(60)

# 4. Salir
pygame.quit()
