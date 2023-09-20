import pygame
import sys
from Constantes import *
from datos import lista_preguntas

pygame.init()

color_rectangulo_pregunta = COLOR_AMARILLO
color_rectangulo_reiniciar = COLOR_AMARILLO
puntaje = 0
contador_diccionarios = 0
rectangulo_pregunta = pygame.Rect(300, 20, 200, 100)
rectangulo_reiniciar = pygame.Rect(300, 450, 200, 100)
rectangulo_opcion_a = pygame.Rect(10, 350, 230, 50)
rectangulo_opcion_b = pygame.Rect(290, 350, 230, 50)
rectangulo_opcion_c = pygame.Rect(550, 350, 230, 50)
contador_clicks = 0
flag = 0

SCREEN = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mi Preguntados ;)")

image = pygame.image.load("Mi_preguntados\imagen preguntados.png")
image = pygame.transform.scale(image,(200, 200))

fuente = pygame.font.SysFont("Arial", 30)
texto_reiniciar = fuente.render("REINICIAR", True, COLOR_GRIS)
texto_pregunta = fuente.render("PREGUNTA", True, COLOR_GRIS)
texto_score = fuente.render("SCORE", True, COLOR_GRIS)
texto_puntaje = fuente.render(str(puntaje), True, COLOR_GRIS)
texto_preguntas = fuente.render(lista_preguntas[contador_diccionarios]['pregunta'], True, COLOR_GRIS)
texto_opcion_a = fuente.render(lista_preguntas[contador_diccionarios]['a'], True, COLOR_AZUL)
texto_opcion_b = fuente.render(lista_preguntas[contador_diccionarios]['b'], True, COLOR_AZUL)
texto_opcion_c = fuente.render(lista_preguntas[contador_diccionarios]['c'], True, COLOR_AZUL)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        texto_preguntas = fuente.render(lista_preguntas[contador_diccionarios]['pregunta'], True, COLOR_GRIS)
        texto_opcion_a = fuente.render(lista_preguntas[contador_diccionarios]['a'], True, COLOR_AZUL)
        texto_opcion_b = fuente.render(lista_preguntas[contador_diccionarios]['b'], True, COLOR_AZUL)
        texto_opcion_c = fuente.render(lista_preguntas[contador_diccionarios]['c'], True, COLOR_AZUL)
        texto_puntaje = fuente.render(str(puntaje), True, COLOR_GRIS)

        if event.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(event.pos)
            #RESPUESTA 'A' -------------------------------------------------------------------------------------------------
            if lista_preguntas[contador_diccionarios]['correcta'] == 'a':
                if rectangulo_opcion_a.collidepoint(event.pos):
                    flag = 0
                    contador_clicks = 0
                    if contador_diccionarios == len(lista_preguntas)-1:
                        contador_diccionarios = 0
                        puntaje = 0
                    else: 
                        contador_diccionarios += 1
                        puntaje += 10
                elif rectangulo_opcion_b.collidepoint(event.pos):
                    flag = 1
                    contador_clicks += 1
                elif rectangulo_opcion_c.collidepoint(event.pos):
                    flag = 2
                    contador_clicks += 1

                if flag == 1:
                    rectangulo_opcion_b = pygame.Rect(0, 0, 0, 0)
                elif flag == 2:
                    rectangulo_opcion_c = pygame.Rect(0, 0, 0, 0)
                else:
                    rectangulo_opcion_b = pygame.Rect(290, 350, 230, 50)
                    rectangulo_opcion_c = pygame.Rect(550, 350, 230, 50)    

            #RESPUESTA 'B' -------------------------------------------------------------------------------------------------
            elif lista_preguntas[contador_diccionarios]['correcta'] == 'b':
                if rectangulo_opcion_b.collidepoint(event.pos): 
                    flag = 0
                    contador_clicks = 0
                    if contador_diccionarios == len(lista_preguntas)-1:
                        contador_diccionarios = 0
                        puntaje = 0
                    else: 
                        contador_diccionarios += 1
                        puntaje += 10
                elif rectangulo_opcion_a.collidepoint(event.pos):
                    flag = 1
                    contador_clicks += 1
                elif rectangulo_opcion_c.collidepoint(event.pos):
                    flag = 2
                    contador_clicks += 1

                if flag == 1:
                    rectangulo_opcion_a = pygame.Rect(0, 0, 0, 0)
                elif flag == 2:
                    rectangulo_opcion_c = pygame.Rect(0, 0, 0, 0)
                else:
                    rectangulo_opcion_a = pygame.Rect(10, 350, 230, 50)
                    rectangulo_opcion_c = pygame.Rect(550, 350, 230, 50)

            #RESPUESTA 'C' -------------------------------------------------------------------------------------------------
            elif lista_preguntas[contador_diccionarios]['correcta'] == 'c':
                if rectangulo_opcion_c.collidepoint(event.pos):
                    flag = 0
                    contador_clicks = 0
                    if contador_diccionarios == len(lista_preguntas)-1:
                        contador_diccionarios = 0
                        puntaje = 0
                    else: 
                        contador_diccionarios += 1
                        puntaje += 10
                elif rectangulo_opcion_a.collidepoint(event.pos):
                    flag = 1
                    contador_clicks += 1
                elif rectangulo_opcion_b.collidepoint(event.pos):
                    flag = 2
                    contador_clicks += 1

                if flag == 1:
                    rectangulo_opcion_a = pygame.Rect(0, 0, 0, 0)
                elif flag == 2:
                    rectangulo_opcion_b = pygame.Rect(0, 0, 0, 0)
                else:
                    rectangulo_opcion_a = pygame.Rect(10, 350, 230, 50)
                    rectangulo_opcion_b = pygame.Rect(290, 350, 230, 50)

            if contador_clicks == 2:
                if contador_diccionarios == len(lista_preguntas)-1:
                    contador_diccionarios = 0
                    puntaje = 0
                else: 
                    contador_diccionarios += 1
                rectangulo_opcion_a = pygame.Rect(10, 350, 230, 50)
                rectangulo_opcion_b = pygame.Rect(290, 350, 230, 50)
                rectangulo_opcion_c = pygame.Rect(550, 350, 230, 50)
                contador_clicks = 0
                
            #rectangulo pregunta
            if rectangulo_pregunta.collidepoint(event.pos):
                rectangulo_opcion_a = pygame.Rect(10, 350, 230, 50)
                rectangulo_opcion_b = pygame.Rect(290, 350, 230, 50)
                rectangulo_opcion_c = pygame.Rect(550, 350, 230, 50)
                contador_clicks = 0
                if contador_diccionarios == len(lista_preguntas)-1:
                    contador_diccionarios = 0
                    puntaje = 0
                else: 
                    contador_diccionarios += 1
            #rectangulo reiniciar
            if rectangulo_reiniciar.collidepoint(event.pos):
                contador_diccionarios = 0
                puntaje = 0
                contador_clicks = 0
                rectangulo_opcion_a = pygame.Rect(10, 350, 230, 50)
                rectangulo_opcion_b = pygame.Rect(290, 350, 230, 50)
                rectangulo_opcion_c = pygame.Rect(550, 350, 230, 50)
                flag = 0

    SCREEN.fill(COLOR_AZUL)
    pygame.draw.rect(SCREEN, color_rectangulo_pregunta, rectangulo_pregunta)
    pygame.draw.rect(SCREEN, color_rectangulo_reiniciar, rectangulo_reiniciar) 
    pygame.draw.rect(SCREEN, COLOR_AMARILLO, rectangulo_opcion_a) 
    pygame.draw.rect(SCREEN, COLOR_AMARILLO, rectangulo_opcion_b)
    pygame.draw.rect(SCREEN, COLOR_AMARILLO, rectangulo_opcion_c)
    
    posicion_mouse = pygame.mouse.get_pos()
    list(posicion_mouse)
    #rectangulo pregunta
    if (posicion_mouse[0] > 300 and posicion_mouse[0] < 500) and (posicion_mouse[1] > 20 and posicion_mouse[1] < 120):
        color_rectangulo_pregunta = COLOR_VERDE
    else:
        color_rectangulo_pregunta = COLOR_AMARILLO
    #rectangulo reinicar
    if (posicion_mouse[0] > 300 and posicion_mouse[0] < 500) and (posicion_mouse[1] > 450 and posicion_mouse[1] < 550):
        color_rectangulo_reiniciar = COLOR_VERDE
    else:
        color_rectangulo_reiniciar = COLOR_AMARILLO
    
    SCREEN.blit(image, (10, 10))
    SCREEN.blit(texto_score, (330, 170))
    SCREEN.blit(texto_puntaje, (330, 195))
    SCREEN.blit(texto_pregunta, (340, 50))
    SCREEN.blit(texto_reiniciar, (340, 480))
    SCREEN.blit(texto_preguntas, (20, 250))
    SCREEN.blit(texto_opcion_a, (20, 350))
    SCREEN.blit(texto_opcion_b, (300, 350))
    SCREEN.blit(texto_opcion_c, (560, 350))

    pygame.display.flip()