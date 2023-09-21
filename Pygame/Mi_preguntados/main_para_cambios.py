import pygame
import sys
from Constantes import *
from datos import lista_preguntas

pygame.init()

color_rectangulo_pregunta = COLOR_AMARILLO
color_rectangulo_reiniciar = COLOR_AMARILLO
color_rectangulo_opcion_a = COLOR_AMARILLO
color_rectangulo_opcion_b = COLOR_AMARILLO
color_rectangulo_opcion_c = COLOR_AMARILLO
color_texto_opciones = COLOR_AZUL
puntaje = 0
contador_diccionarios = 0
rectangulo_pregunta = pygame.Rect(300, 20, 200, 100)
rectangulo_reiniciar = pygame.Rect(300, 450, 200, 100)
rectangulo_opcion_a = pygame.Rect(10, 350, 230, 50)
rectangulo_opcion_b = pygame.Rect(290, 350, 230, 50)
rectangulo_opcion_c = pygame.Rect(550, 350, 230, 50)
rectangulo_opcion_a_normal = pygame.Rect(10, 350, 230, 50)
rectangulo_opcion_b_normal = pygame.Rect(290, 350, 230, 50)
rectangulo_opcion_c_normal = pygame.Rect(550, 350, 230, 50)
rectangulo_inexistente = pygame.Rect(0, 0, 0, 0)
contador_clicks = 0
flag = 0

SCREEN = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mi Preguntados ;)")

image = pygame.image.load(RUTA_IMAGEN)
image = pygame.transform.scale(image,(200, 200))

fuente = pygame.font.SysFont("Arial", 30)
texto_reiniciar = fuente.render("REINICIAR", True, COLOR_GRIS)
texto_pregunta = fuente.render("PREGUNTA", True, COLOR_GRIS)
texto_score = fuente.render("SCORE", True, COLOR_GRIS)
texto_puntaje = fuente.render(str(puntaje), True, COLOR_GRIS)
texto_preguntas = fuente.render(lista_preguntas[contador_diccionarios]['pregunta'], True, COLOR_GRIS)
texto_opcion_a = fuente.render(lista_preguntas[contador_diccionarios]['a'], True, color_texto_opciones)
texto_opcion_b = fuente.render(lista_preguntas[contador_diccionarios]['b'], True, color_texto_opciones)
texto_opcion_c = fuente.render(lista_preguntas[contador_diccionarios]['c'], True, color_texto_opciones)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        texto_preguntas = fuente.render(lista_preguntas[contador_diccionarios]['pregunta'], True, COLOR_GRIS)
        texto_opcion_a = fuente.render(lista_preguntas[contador_diccionarios]['a'], True, color_texto_opciones)
        texto_opcion_b = fuente.render(lista_preguntas[contador_diccionarios]['b'], True, color_texto_opciones)
        texto_opcion_c = fuente.render(lista_preguntas[contador_diccionarios]['c'], True, color_texto_opciones)
        texto_puntaje = fuente.render(str(puntaje), True, COLOR_GRIS)
        respuesta_correcta = lista_preguntas[contador_diccionarios]['correcta']

        if event.type == pygame.MOUSEBUTTONDOWN:
            #RESPUESTA 'A' -------------------------------------------------------------------------------------------------
            if respuesta_correcta == 'a':
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
                    rectangulo_opcion_b = rectangulo_inexistente
                elif flag == 2:
                    rectangulo_opcion_c = rectangulo_inexistente
                else:
                    rectangulo_opcion_b = rectangulo_opcion_b_normal
                    rectangulo_opcion_c = rectangulo_opcion_c_normal  

            #RESPUESTA 'B' -------------------------------------------------------------------------------------------------
            elif respuesta_correcta == 'b':
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
                    rectangulo_opcion_a = rectangulo_inexistente
                elif flag == 2:
                    rectangulo_opcion_c = rectangulo_inexistente
                else:
                    rectangulo_opcion_a = rectangulo_opcion_a_normal
                    rectangulo_opcion_c = rectangulo_opcion_c_normal

            #RESPUESTA 'C' -------------------------------------------------------------------------------------------------
            elif respuesta_correcta == 'c':
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
                    rectangulo_opcion_a = rectangulo_inexistente
                elif flag == 2:
                    rectangulo_opcion_b = rectangulo_inexistente
                else:
                    rectangulo_opcion_a = rectangulo_opcion_a_normal
                    rectangulo_opcion_b = rectangulo_opcion_b_normal

            if contador_clicks == 2:
                if contador_diccionarios == len(lista_preguntas)-1:
                    contador_diccionarios = 0
                    puntaje = 0
                else: 
                    contador_diccionarios += 1
                rectangulo_opcion_a = rectangulo_opcion_a_normal
                rectangulo_opcion_b = rectangulo_opcion_b_normal
                rectangulo_opcion_c = rectangulo_opcion_c_normal
                contador_clicks = 0
                flag = 0
                
            #rectangulo pregunta
            if rectangulo_pregunta.collidepoint(event.pos):
                rectangulo_opcion_a = rectangulo_opcion_a_normal
                rectangulo_opcion_b = rectangulo_opcion_b_normal
                rectangulo_opcion_c = rectangulo_opcion_c_normal
                contador_clicks = 0
                if contador_diccionarios == len(lista_preguntas)-1:
                    contador_diccionarios = 0
                    puntaje = 0
                else: 
                    contador_diccionarios += 1
                flag = 0
            #rectangulo reiniciar
            if rectangulo_reiniciar.collidepoint(event.pos):
                contador_diccionarios = 0
                puntaje = 0
                contador_clicks = 0
                rectangulo_opcion_a = rectangulo_opcion_a_normal
                rectangulo_opcion_b = rectangulo_opcion_b_normal
                rectangulo_opcion_c = rectangulo_opcion_c_normal
                flag = 0

    SCREEN.fill(COLOR_AZUL)
    pygame.draw.rect(SCREEN, color_rectangulo_pregunta, rectangulo_pregunta)
    pygame.draw.rect(SCREEN, color_rectangulo_reiniciar, rectangulo_reiniciar) 
    pygame.draw.rect(SCREEN, color_rectangulo_opcion_a, rectangulo_opcion_a) 
    pygame.draw.rect(SCREEN, color_rectangulo_opcion_b, rectangulo_opcion_b)
    pygame.draw.rect(SCREEN, color_rectangulo_opcion_c, rectangulo_opcion_c)
    

    posicion_mouse = pygame.mouse.get_pos()
    if rectangulo_pregunta.collidepoint(posicion_mouse):
        color_rectangulo_pregunta = COLOR_VERDE
    elif rectangulo_reiniciar.collidepoint(posicion_mouse):
        color_rectangulo_reiniciar = COLOR_VERDE
    elif rectangulo_opcion_a.collidepoint(posicion_mouse):
        color_rectangulo_opcion_a = COLOR_VERDE
    elif rectangulo_opcion_b.collidepoint(posicion_mouse):
        color_rectangulo_opcion_b = COLOR_VERDE
    elif rectangulo_opcion_c.collidepoint(posicion_mouse):
        color_rectangulo_opcion_c = COLOR_VERDE
    else:
        color_rectangulo_pregunta = COLOR_AMARILLO
        color_rectangulo_reiniciar = COLOR_AMARILLO
        color_rectangulo_opcion_a = COLOR_AMARILLO
        color_rectangulo_opcion_b = COLOR_AMARILLO
        color_rectangulo_opcion_c = COLOR_AMARILLO
    
    
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