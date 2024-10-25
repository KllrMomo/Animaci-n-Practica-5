import pygame
import math

#inicializar Pygame
pygame.init()

#definir colores
BLANCO = (255, 255, 255)
ROSA = (243, 58, 106)

# Configuración de la ventana
ancho_ventana = 500
alto_ventana = 500
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Movimiento Curvilíneo")

# Función para obtener el ángulo (theta)
def obtenerAngulo(tiempo):
    return (tiempo * math.pi / 5)*-1  # El tiempo en radianes

# Función para obtener el radio (r), vamos a escalarlo para hacerlo más visible
def obtenerR(tiempo):
    return 200 * math.sin(tiempo * math.pi / 5)  # Escalar r por 200 para mayor visibilidad

# Loop principal
ejecutando = True
tiempo = 0

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Calcular posición
    theta = obtenerAngulo(tiempo)
    r = obtenerR(tiempo)
    x = int(ancho_ventana/2 + r * math.cos(theta))  # Coordenada x
    y = int(alto_ventana/2 + r * math.sin(theta))   # Coordenada y

    # Dibujar en la ventana
    ventana.fill(BLANCO)
    pygame.draw.line(ventana, ROSA, (ancho_ventana/2, alto_ventana/2), (x, y), 2)
    pygame.draw.circle(ventana, ROSA, (x, y), 5)

    # Actualizar la pantalla
    pygame.display.flip()

    # Incrementar tiempo
    tiempo += 0.1
    pygame.time.delay(100)  # Retardar para suavizar la animación

pygame.quit()