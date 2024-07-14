import pygame
import os

class pantalla():
    
    def __init__(self,ancho,alto,botones,mouse) -> None:
        self.ancho = ancho
        self.alto = alto
        self.botones = botones
        self.mouse = mouse
        self.comienzo_escritura = self.botones[0].ancho
        self.archivo_txt = ""
        self.tamaño_letra = 25
        self.input = ""
        self.momento = "menu"
        self.archivo = ""
        self.linea_inicial = 0
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
            x = self.comienzo_escritura
            ancho = self.ancho - self.comienzo_escritura
            y = 0
            palabras = self.input.split(" ")
        elif self.momento == "guardar":
            x = 0
            ancho = self.ancho
            y = self.tamaño_letra
            palabras = self.archivo.split(" ")
        
        lineas = []
        linea_actual = []
        ancho_Total = 0
        
        for palabra in palabras:
            ancho_palabra, _ = self.myFond.size(palabra + " ")
            
            if ancho_Total + ancho_palabra <= ancho and "\n" not in palabra:
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
        
        for linea in lineas[self.linea_inicial : self.cantidad_lineas]:
            self._dibujarTexto(linea,x,y)
            y += self.tamaño_letra

    def manejo_evento(self,event):
        """
        Manejo de evento, aca se encagara de escribir en pantalla.
        """
        if event.type == pygame.TEXTINPUT:
            if self.momento == "texto":
                self.input += event.text
            elif self.momento in ["guardar", "abrir"]:
                self.archivo += event.text
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = event.button
            for boton in self.botones:
                boton.accion(self.mouse,click,self)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if self.momento == "texto":
                    self.input = self.input[:-1]
                elif self.momento in ["guardar", "abrir"]:
                    self.archivo = self.archivo[:-1]
            elif event.key == pygame.K_RETURN:
                if self.momento == "texto":
                    self.input += " \n"
                elif self.momento == "guardar":
                    if self.comprobacion_archivo():
                        self.guardado()
                    self.momento = "texto"
                elif self.momento == "abrir":
                    self.momento = "archivo"
            elif event.key == pygame.K_RIGHT:
                if self.momento == "texto":
                    self.linea_inicial += 1
                    self.cantidad_lineas += 1
            elif event.key == pygame.K_LEFT:
                if self.momento == "texto" and self.linea_inicial > 0:
                    self.linea_inicial -= 1
                    self.cantidad_lineas -= 1

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
    
    def abrir(self):
        """
        Esa funcion sirve para mostrar en pantalla todos los archivos de la ubicacion actual del programa
        """
        archivos = os.listdir()
        archivo_txt = ""
        for archivo in archivos:
            if ".txt" in archivo or ".docx" in archivo or ".doc" in archivo:
                if archivo_txt == "":
                    archivo_txt += archivo
                else:
                    archivo_txt += " " + archivo

        self.archivo_txt = archivo_txt

        if self.archivo_txt == "":
            self.botones[3].dibujar(self.screen, self.mouse)
            self._dibujarTexto("No hay ningun archivo",0,0)
        else:
            self._dibujarTexto(self.archivo,0,0)
            y = self.tamaño_letra
            self._dibujarTexto(self.archivo_txt,0,y)

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
        self.botones[0].dibujar(self.screen,self.mouse)
        self.botones[1].dibujar(self.screen,self.mouse)
    
    def dibujar(self):
        """
        Se encarga de dibujar todo el contenido necesario en pantalla
        """
        self.screen.fill("black")
        
        if self.momento == "menu":
            self.menu()
        
        if self.momento == "abrir":
            self.abrir()
        
        if self.momento == "archivo":
            self.input = self.abrir_archivo()
            self.momento = "texto"
        
        if self.momento == "texto":
            self.botones[2].dibujar(self.screen,self.mouse)
            self.botones[3].dibujar(self.screen,self.mouse)
            self.manejo_texto()

        if self.momento == "guardar":
            self._dibujarTexto("Ingrese el nombre del archivo",0,0)
            self.manejo_texto()