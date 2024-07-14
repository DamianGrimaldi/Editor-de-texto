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

    def _dibujarTexto(self,texto,altura):
        texto = self.myFond.render(texto,True,(255,255,255))
        self.screen.blit(texto,(0,altura))

    def manejo_texto(self):
        """
        Se encarga de mostrar en pantalla el texto ingresado por el usuario.add()
        """
        palabras = self.input.split(" ")
        lineas = []
        linea_actual = []
        ancho_Total = 0
        
        for palabra in palabras:
            ancho_palabra, _ = self.myFond.size(palabra + " ")
            
            if ancho_Total + ancho_palabra <= self.ancho and "\n" not in palabra:
                linea_actual.append(palabra)
                ancho_Total += ancho_palabra
            else:
                subpalabra = palabra.split("\n")
                if linea_actual:
                    lineas.append(" ".join(linea_actual))
                linea_actual = [subpalabra[0]]
                ancho_Total = ancho_palabra
        
        if linea_actual:
            lineas.append(" ".join(linea_actual))
        
        y = 0
        
        if len(lineas) > self.cantidad_lineas:
            for linea in lineas[-self.cantidad_lineas:]:
                self._dibujarTexto(linea,y)
                y += self.tamaño_letra
        
        else:
            for linea in lineas:
                self._dibujarTexto(linea,y)
                y += self.tamaño_letra

    def manejo_evento(self,event):
        """
        Manejo de evento, aca se encagara de escribir en pantalla.
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
        
        self.manejo_texto()