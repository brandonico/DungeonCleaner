import pygame
import random
import os
from vista.enemigo_grafico import EnemigoGrafico

class MundoGrafico:
    """
    Clase que representa el mundo gráfico del juego.
    """

    def __init__(self, ancho: int, alto: int, ventana: pygame.Surface):
        """
        Inicializa el mundo gráfico con un tamaño específico.

        :param ancho: Ancho de la ventana.
        :param alto: Alto de la ventana.
        """
        self.ancho = ancho
        self.alto = alto
        self.fondo = (0, 255, 0)# Color de fondo (verde)
        self.ventana = ventana
        imagen_path = os.path.join("recursos", "implementado", "fondos", "cesped.png")
        if not os.path.exists(imagen_path):  # Verifica si el archivo existe
            raise FileNotFoundError(f"No se encontró el archivo de imagen: {imagen_path}")  
        self.imagen = pygame.image.load(imagen_path).convert_alpha()  
        self.imagen = pygame.transform.scale(self.imagen,size=(64,64)) 
        
        
        pygame.display.set_caption("Mundo Gráfico")  # Título de la ventana

    def dibujar_fondo(self, pantalla):    
        """
        Dibuja el fondo de la ventana.
        """
       # self.ventana.fill(self.fondo)
        for y in range(0,self.alto,64): 
            for x in range(0,self.ancho,64): 
                pantalla.blit(self.imagen, (x, y))

    

    def crear_enemigos(self, cantidad):
        """
        Crea un grupo de enemigos en posiciones aleatorias dentro del mundo.

        :param cantidad: Número de enemigos a crear.
        """
        self.enemigos = pygame.sprite.Group()
        for _ in range(cantidad):
            x = random.randint(0, self.ancho - 50)
            y = random.randint(0, self.alto - 45)
            color = (255, 0, 0)  # o el color que prefieras
            modelo = None  # o tu modelo lógico de enemigo
            enemigo = EnemigoGrafico(x, y, color, modelo)
            self.enemigos.add(enemigo)
