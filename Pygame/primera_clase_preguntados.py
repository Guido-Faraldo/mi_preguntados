from data_stark import lista_personajes
import pygame
from Mi_preguntados.Constantes import *
from Mi_preguntados.datos import lista


pygame.init()

titulo = ""
posicion = 0
lista_nombre = []
for heroe in lista_personajes:
    lista_nombre.append(heroe['nombre'])

SCREEN = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Pygame")

#DEFINIMOS IMAGEN
# image = pygame.image.load("...")
# image = pygame.transform.scale(image,(80, 80))

#DEFINIMOS TEXTO
fuente = pygame.font.SysFont("Arial", 30)
texto_titulo = fuente.render(str(titulo), True, COLOR_GRIS)






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(event.pos)
            print(posicion_click)
            if (posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 20 and posicion_click[1] < 120):
                titulo = lista_nombre[posicion]
                texto_titulo = fuente.render(str(titulo), True, COLOR_VERDE)
                if posicion >= len(lista_nombre) -1 :
                    posicion = 0
                else: 
                    posicion += 1





    SCREEN.fill(COLOR_ROJO)
    pygame.draw.rect(SCREEN, COLOR_BLANCO, (300, 20, 200, 100)) #distancia desde la izquierda, distancia desde arriba, ancho, largo 
    # SCREEN.blit(image, (30, 100))
    SCREEN.blit(texto_titulo, (150, 170))
    pygame.display.flip()
