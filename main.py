import pygame
import sys
from pantalla.pantalla import *
from boton.boton import *

pygame.init()

ancho = 800
alto = 600

botones = []
ancho_boton = 200
alto_boton = 100
color_inactivo = (122,22,22)
color_activo = (22,22,122)
posicion_menu_X = (ancho - ancho_boton)//2
posicion_menu_Y = alto //2 - alto_boton
posiciones = [(posicion_menu_X,posicion_menu_Y),(posicion_menu_X, posicion_menu_Y + alto_boton +10), (0,10),(0,alto_boton+20)]
valores = ["abrir","crear","guardar","salir"]

for i in range(4):
    boton = Boton(posiciones[i][0],posiciones[i][1],ancho_boton,alto_boton,color_inactivo,color_activo,valores[i])
    botones.append(boton)

mouse = pygame.mouse

screen = pantalla(ancho,alto,botones,mouse)

pygame.display.set_caption("Editor de texto")
reloj = pygame.time.Clock()

def manejo_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.manejo_evento(event)

def actualizar_pantalla():
    
    screen.dibujar()
    
    pygame.display.flip()

def main():
    
    pygame.key.start_text_input() #Esto sirve para manejo del input
    
    while True:
        
        manejo_eventos()
        
        reloj.tick(60)
        
        actualizar_pantalla()

    pygame.key.stop_text_input()

main()