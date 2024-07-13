import pygame
import os

class pantalla():
    
    def __init__(self,ancho,alto) -> None:
        self.ancho = ancho
        self.alto = alto
        self.tamaño_letra = 25
        self.input = ""
        self.cantidad_lineas = self.alto // self.tamaño_letra
        self.myFond = pygame.font.SysFont('Times New Roman', self.tamaño_letra)
        self.screen = pygame.display.set_mode((self.ancho,self.alto))
    
    def manejo_texto(self):
        """
        Se encarga de mostrar en pantalla el texto ingresado por el usuario.add()
        """
        pass
    
    def manejo_teclas(self,key):
        """
        Manejo del teclado, para guardar el archivo es control + g
        """
        pass
    
    def comprobacion_archivo(self):
        """
        Aca va a validar si hay cambios con respecto al archivo
        """
        pass
    
    def guardado(self):
        """
        Se encarga de guardar el contenido en el archivo
        """
        pass
    
    def abrir_archivo(self):
        """
        Se encarga de abrir y tanscribir el contenido en el input para el usuario
        """
        pass
    
    def menu(self):
        """
        Elegir entre dos estado, abrir un archivo ya existente, o crear uno nuevo
        """
        pass
    
    def dibujar(self):
        """
        Se encarga de dibujar todo el contenido necesario en pantalla
        """
        self.screen.fill("black")