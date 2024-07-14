import pygame
import os

class pantalla():
    
    def __init__(self,ancho,alto) -> None:
        self.ancho = ancho
        self.alto = alto
        self.tamaño_letra = 25
        self.input = ""
        self.momento = "guardado"
        self.archivo = ""
        self.cantidad_lineas = self.alto // self.tamaño_letra
        self.myFond = pygame.font.SysFont('Times New Roman', self.tamaño_letra)
        self.screen = pygame.display.set_mode((self.ancho,self.alto))

    def _dibujarTexto(self,texto,anchura,altura):
        texto = self.myFond.render(texto,True,(255,255,255))
        self.screen.blit(texto,(anchura,altura))

    def manejo_texto(self):
        """
        Se encarga de mostrar en pantalla el texto ingresado por el usuario.add()
        """
        if self.momento == "texto":
            palabras = self.input.split(" ")
        elif self.momento == "guardado":
            palabras = self.archivo.split(" ")
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
                linea_actual = [subpalabra[1]]
                ancho_Total = ancho_palabra
        
        if linea_actual:
            lineas.append(" ".join(linea_actual))
        
        y = 0
        
        if len(lineas) > self.cantidad_lineas:
            for linea in lineas[-self.cantidad_lineas:]:
                self._dibujarTexto(linea,0,y)
                y += self.tamaño_letra
        
        else:
            for linea in lineas:
                self._dibujarTexto(linea,0,y)
                y += self.tamaño_letra

    def manejo_evento(self,event):
        """
        Manejo de evento, aca se encagara de escribir en pantalla.
        """
        if event.type == pygame.TEXTINPUT:
            if self.momento == "texto":
                self.input += event.text
            elif self.momento == "guardado":
                self.archivo += event.text
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if self.momento == "texto":
                    self.input = self.input[:-1]
                elif self.momento == "guardado":
                    self.archivo = self.archivo[:-1]
            elif event.key == pygame.K_RETURN:
                if self.momento == "texto":
                    self.input += " \n"
                elif self.momento == "guardado":
                    if self.comprobacion_archivo():
                        self.guardado()
                    self.momento = "texto"

    def manejo_teclas(self,key):
        """
        Manejo del teclado, para guardar el archivo es control + g
        """
        pass
    
    def comprobacion_archivo(self):
        """
        Aca va a validar si hay cambios con respecto al archivo.
        Primero evalua si existe el archivo, y si existe, comprueba si existe algun cambio antes de guardar. y si existe, entonces prosigue a cambiarlo.
        En el caso de que no exista el archivo, retorna True.
        """
        if os.path.exists(self.archivo):
            archivo_temporal = self.abrir_archivo()
            if self.input != archivo_temporal:
                return True
        else:
            return True
        return False
    
    def guardado(self):
        """
        Se encarga de guardar el contenido en el archivo
        """
        with open(self.archivo,"w", encoding="utf-8") as file:
            file.write(self.input)
    
    def abrir_archivo(self):
        """
        Se encarga de abrir y tanscribir el contenido en el input para el usuario
        """
        with open(self.archivo, "r", encoding="utf-8") as file:
            archivo = file.read()
        
        return archivo
    
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
        
        if self.momento == "menu":
            self.menu()
        
        if self.momento == "archivo":
            self.archivo = self.abrir_archivo()
            self.momento = "texto"
        
        if self.momento in ["texto", "guardado"]:
            self.manejo_texto()