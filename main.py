import pygame
import sys
from pantalla.pantalla import *

pygame.init()

ancho = 800
alto = 600

screen = pantalla(ancho,alto)

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