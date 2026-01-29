import sys
import subprocess

try:
    import pygame
except ImportError:
    print("¡Pygame no está instalado! Instalando automáticamente... 🔧")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame
    print("¡Instalación completada! Arrancando el juego... 🚀")

# 1. Inicializar Pygame
# Siempre es el primer paso. Prepara los módulos internos.
pygame.init()

# 2. Configuración de la Pantalla

ANCHO = 800
ALTO = 600
# Creamos la ventana (Superficie principal)
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("")

# Reloj para controlar la velocidad del juego (FPS)
reloj = pygame.time.Clock()

# Variable para controlar el bucle principal
corriendo = True
jugador_x = 100
jugador_y = 100
# Cargar la imagen desde el archivo
imagen_jugador = pygame.image.load("jugador.png")
enemigo_x = 600
enemigo_y = 400
imagen_enemigo = pygame.image.load("enemigo.png")
# Opcional: Si es muy grande/pequeña, se puede cambiar el tamaño.
# imagen_jugador = pygame.transform.scale(imagen_jugador, (50, 50)) 
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
    pantalla.fill((0, 0, 0))  # RGB: (0, 0, 0) es Negro
    pantalla.blit(imagen_jugador, (jugador_x, jugador_y))
    pantalla.blit(imagen_enemigo, (enemigo_x, enemigo_y))
    # Actualizamos la pantalla para mostrar lo que hemos dibujado
    pygame.display.flip()

    # Controlamos los FPS (60 imágenes por segundo)
    reloj.tick(60)

# 4. Salir
pygame.quit()
